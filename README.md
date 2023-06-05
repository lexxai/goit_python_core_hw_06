# goit_python_core_hw_06

File structure before:
```
└───test_tree
    │   file0-0-1.jpg
    │   file0-0-2.zip
    │
    ├───tree1
    │   ├───tree1-1
    │   │       file1-1-1.jpg
    │   │       file1-1-2.zip
    │   │
    │   └───tree1-2
    │           file1-2-1.jpg
    │           file1-2-2.zip
    │           відео-1-2-3.mp4
    │
    └───tree2
        │   file0-2-1.jpg
        │   file0-2-2.zip
        │
        ├───tree2-1
        │       file2-1-1.jpg
        │       file2-1-2.zip
        │       file2-1-3.rrr
        │       відео.mp4
        │       документ-2-1-3.doc
        │
        └───tree2-2
                file2-2-2.zip
                відео.mp4
```


```
> python sort.py 
path is not defined by args, used default: test_tree
Exception unpack with file "file1-1-2.zip": test_tree\archive\file1-1-2.zip is not a zip file
Exception unpack with file "file1-2-2.zip": test_tree\archive\file1-2-2.zip is not a zip file
{
'found_files_by_type': {
  'images': [WindowsPath('test_tree/file0-0-1.jpg'), WindowsPath('test_tree/tree1/tree1-1/file1-1-1.jpg'), WindowsPath('test_tree/tree1/tree1-2/file1-2-1.jpg'), WindowsPath('test_tree/tree2/file0-2-1.jpg'), WindowsPath('test_tree/tree2/tree2-1/file2-1-1.jpg')], 
  'archive': [WindowsPath('test_tree/file0-0-2.zip'), WindowsPath('test_tree/tree1/tree1-1/file1-1-2.zip'), WindowsPath('test_tree/tree1/tree1-2/file1-2-2.zip'), WindowsPath('test_tree/tree2/file0-2-2.zip'), WindowsPath('test_tree/tree2/tree2-1/file2-1-2.zip'), WindowsPath('test_tree/tree2/tree2-2/file2-2-2.zip')], 
  'video': [WindowsPath('test_tree/tree1/tree1-2/відео-1-2-3.mp4'), WindowsPath('test_tree/tree2/tree2-1/відео.mp4'), WindowsPath('test_tree/tree2/tree2-2/відео.mp4')], 
  'others': [WindowsPath('test_tree/tree2/tree2-1/file2-1-3.rrr')], 
  'documents': [WindowsPath('test_tree/tree2/tree2-1/документ-2-1-3.doc')]
 }, 
'found_extensions': {'known': {'DOC', 'ZIP', 'MP4', 'JPG'}, 'unknown': {'RRR'}}
}
```

File structure after:
```
└───test_tree
    ├───archive
    │   │   file1-1-2.zip
    │   │   file1-2-2.zip
    │   │
    │   ├───file0-0-2
    │   │       file0-0-2.txt
    │   │
    │   ├───file0-2-2
    │   │       file0-2-2.txt
    │   │
    │   ├───file1-1-2
    │   ├───file1-2-2
    │   ├───file2-1-2
    │   │       file2-1-2.ext.sh
    │   │
    │   └───file2-2-2
    │           file2-2-2.bin
    │
    ├───documents
    │       dokument-2-1-3.doc
    │
    ├───images
    │       file0-0-1.jpg
    │       file0-2-1.jpg
    │       file1-1-1.jpg
    │       file1-2-1.jpg
    │       file2-1-1.jpg
    │
    ├───others
    │       file2-1-3.rrr
    │
    └───video
            video-1-2-3.mp4
            video.mp4
            video_f6c2c1b9-29b1-4edc-adc0-dd7c25fd96b6.mp4
```
