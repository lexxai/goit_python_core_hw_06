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

List before moving:
test_tree\file0-0-1.jpg
test_tree\file0-0-2.zip
test_tree\tree1\tree1-1\file1-1-1.jpg
test_tree\tree1\tree1-1\file1-1-2.zip
test_tree\tree1\tree1-2\file1-2-1.jpg
test_tree\tree1\tree1-2\file1-2-2.zip
test_tree\tree1\tree1-2\відео-1-2-3.mp4
test_tree\tree2\file0-2-1.jpg
test_tree\tree2\file0-2-2.zip
test_tree\tree2\tree2-1\file2-1-1.jpg
test_tree\tree2\tree2-1\file2-1-2.zip
test_tree\tree2\tree2-1\file2-1-3.rrr
test_tree\tree2\tree2-1\відео.mp4
test_tree\tree2\tree2-1\документ-2-1-3.doc
test_tree\tree2\tree2-2\file2-2-2.zip
test_tree\tree2\tree2-2\відео.mp4

Sorted types before moving:

images: ['test_tree/file0-0-1.jpg', 'test_tree/tree1/tree1-1/file1-1-1.jpg', 'test_tree/tree1/tree1-2/file1-2-1.jpg', 'test_tree/tree2/file0-2-1.jpg', 'test_tree/tree2/tree2-1/file2-1-1.jpg']

archive: ['test_tree/file0-0-2.zip', 'test_tree/tree1/tree1-1/file1-1-2.zip', 'test_tree/tree1/tree1-2/file1-2-2.zip', 'test_tree/tree2/file0-2-2.zip', 'test_tree/tree2/tree2-1/file2-1-2.zip', 'test_tree/tree2/tree2-2/file2-2-2.zip']

video: ['test_tree/tree1/tree1-2/відео-1-2-3.mp4', 'test_tree/tree2/tree2-1/відео.mp4', 'test_tree/tree2/tree2-2/відео.mp4']

others: ['test_tree/tree2/tree2-1/file2-1-3.rrr']

documents: ['test_tree/tree2/tree2-1/документ-2-1-3.doc']

Sorted extensions before moving:
{'known': {'JPG', 'ZIP', 'DOC', 'MP4'}, 'unknown': {'RRR'}}
Exception unpack with file "file1-1-2.zip": test_tree\archive\file1-1-2.zip is not a zip file
Exception unpack with file "file1-2-2.zip": test_tree\archive\file1-2-2.zip is not a zip file

List after moving:
test_tree\archive\file1-1-2.zip
test_tree\archive\file1-2-2.zip
test_tree\archive\file0-0-2\file0-0-2.txt
test_tree\archive\file0-2-2\file0-2-2.txt
test_tree\archive\file2-1-2\file2-1-2.ext.sh
test_tree\archive\file2-2-2\file2-2-2.bin
test_tree\documents\dokument-2-1-3.doc
test_tree\images\file0-0-1.jpg
test_tree\images\file0-2-1.jpg
test_tree\images\file1-1-1.jpg
test_tree\images\file1-2-1.jpg
test_tree\images\file2-1-1.jpg
test_tree\others\file2-1-3.rrr
test_tree\video\video-1-2-3.mp4
test_tree\video\video.mp4
test_tree\video\video_e47ec939-643f-44ce-896c-48c00e4b882c.mp4
```

File structure after:
```
> tree -F
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
            video_e47ec939-643f-44ce-896c-48c00e4b882c.mp4
```
