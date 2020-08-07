# py_module_add

Calling `module add` from Python

## Example

```bash
$ python
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.

>>> import os
>>> import module
>>> os.system("samtools")
sh: samtools: command not found
32512

>>> module.init()
>>> module.add("samtools")
>>> os.system("samtools --version")
samtools 1.8
Using htslib 1.8
Copyright (C) 2018 Genome Research Ltd.
0
```
