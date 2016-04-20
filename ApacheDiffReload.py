#!/usr/bin/env python
import os
import sys
import hashlib
import shutil

#From Stackoverflow
#http://stackoverflow.com/questions/3431825/generating-a-md5-checksum-of-a-file
def GenMd5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()
    

def ExecuteIfDiff(filenew,filebackup):
    if (os.path.isfile(filenew) and os.path.isfile(filebackup)):
        if (GenMd5(filenew) != GenMd5(filebackup)):
            os.system("/etc/init.d/apache2 reload")
            os.remove(filebackup)
            shutil.copy(filenew, filebackup)

    
def main(filenew,filebackup):
    #Compare the two files by MD5.
    #Execute what is needed if there are differences
    #Delete the previous config, copy the new one.
    ExecuteIfDiff(filenew,filebackup)

main(str(sys.argv[1]),str(sys.argv[2]))
