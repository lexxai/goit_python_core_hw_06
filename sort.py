from pathlib import Path
import shutil
import sys
import uuid


TYPES = {
    "video": ("AVI", "MP4", "MOV", "MKV"),
    "images": ("JPEG", "PNG", "JPG", "SVG"),
    "documents": ("DOC", "DOCX", "TXT", "PDF", "XLSX", "PPTX"),
    "music": ("MP3", "OGG", "WAV", "AMR"),
    "archive": ("ZIP", "GZ", "TAR"),
}


CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "h", "d", "e", "e", "zh", "z", "y", "i", "k", "l", "m", "n", "o", "p", "r", "s",
               "t", "u", "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ya", "ye", "i", "yi", "g",)

TRANS = {}


def init_normalize_map():
    for c, t in zip(CYRILLIC_SYMBOLS, TRANSLATION):
        TRANS[ord(c)] = t
        TRANS[ord(c.upper())] = t.upper()


def normalize(name):
    return name.translate(TRANS)


def browse_files(path: Path) -> list:
    p = Path(path)
    files = []
    for i in p.iterdir():
        if i.is_file():
            files.append(i)
    for i in p.iterdir():
        if i.is_dir():
            files.extend(browse_files(i))

    return files


def browse_dirs(path: Path) -> list:
    p = Path(path)
    dirs = []
    for i in p.iterdir():
        if i.is_dir():
            dirs.append(i)
    for i in dirs:
        dirs.extend(browse_dirs(i))

    return dirs


def sort_by_type(files: list, result) -> None:
    types = list(TYPES.keys())
    types.append("others")
    found_ext = result["found_extensions"]
    found_files = result["found_files_by_type"]
    for item_file in files:
        if item_file.parts[1] in types:
            continue
        ext = item_file.suffix.lstrip(".").upper()
        is_found = False
        for k, v in TYPES.items():
            if ext in v:
                found_ext["known"].add(ext)
                el = found_files.get(k, [])
                el.append(item_file)
                found_files[k] = el
                is_found = True
                break
        if not is_found:
            found_ext["unknown"].add(ext)
            k = "others"
            el = found_files.get(k, [])
            el.append(item_file)
            found_files[k] = el


def set_uniq_name(path: Path):
    name_stem = path.stem
    while path.exists():
        path = path.with_stem(f"{name_stem}_{uuid.uuid4()}")
    return path


def move_files_by_types(path: Path, result):
    found_files = result["found_files_by_type"]
    for file_type, files in found_files.items():
        p = Path(path).joinpath(file_type)
        if not p.exists():
            p.mkdir()
            # print("mkdir", file_type, p)
        for f in files:
            fp = p.joinpath(normalize(f.name))
            if file_type == "archive":
                fp = set_uniq_name(fp)
                archive = f.rename(fp)
                extract_dir = p.joinpath(fp.stem)
                if not extract_dir.exists():
                    extract_dir.mkdir()
                try:
                    shutil.unpack_archive(archive, extract_dir)
                except Exception as e:
                    print(f'Exception unpack with file "{archive.name}":', e)
                else:
                    # print("After success unpack_archive remove src file", archive.name)
                    archive.unlink()
            else:
                try:
                    fp = set_uniq_name(fp)
                    f.rename(fp)
                    # print("rename", f, fp)
                except Exception as e:
                    print("Exception move", e)


def purge_empty(source_path: Path):
    path_list = browse_dirs(source_path)
    path_list.reverse()
    for path in path_list:
        if path.exists() and path.is_dir and not any(path.glob("*")):
            # print("PURGE", path)
            try:
                path.rmdir()
            except Exception as e:
                print("Exception remove", e)


def main():
    if len(sys.argv) < 2:
        path = "test_tree"
        print("path is not defined by args, used default:", path)
    else:
        path = sys.argv[1]

    if not Path(path).exists():
        print(f'path "{path}" is not exist, exiting.')
        exit(1)

    result = {
        "found_files_by_type": {},
        "found_extensions": {"known": set(), "unknown": set()},
    }

    init_normalize_map()
    file_list = browse_files(path)
    print("\nList before moving:", *file_list, sep="\n")
    sort_by_type(file_list, result)
    print(
        "\nSorted types before moving:",
        *[
            f"\n{filetype}: {[ item_file.as_posix() for item_file in list_files ]}"
            for filetype, list_files in result["found_files_by_type"].items()
        ],
        sep="\n",
    )
    print("\nSorted extensions before moving:",
          result["found_extensions"], sep="\n")
    move_files_by_types(path, result)
    purge_empty(path)
    file_list = browse_files(path)
    print("\nList after moving:", *file_list, sep="\n")


if __name__ == "__main__":
    main()
