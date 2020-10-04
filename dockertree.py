#!/usr/bin/env python
import os

#list all the Dockerfiles
def listdockerfiles(path,dockerdict):
    fullpath = ""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith("Dockerfile"):
                fromlst = []
#                print(os.path.join(root, file))
                fullpath = os.path.join(root, file)
#Get all the FROMs per dockerfile
                dockerfile = open(fullpath, "r")
                for lines in dockerfile:
#                print(lines)
                    if lines.startswith("FROM "):
                        fromlst.append(lines)
                dockerdict[fullpath] = fromlst

def listafrom(dockerdict,fromdict):
    for dfile,v in dockerdict.items():
#        print(k)
#        print(v)
        for dfrom in v:
#            print(f)
            fromdict[dfrom] = []
            

#Build tree of connections

#Show the tree or export it?
#* Source Image
#** Child of Source
#*** Child of Child

def usage():
	print("Find the tree of images from a given directory")
	print("filedeleter.py -d /home/directory")

def main():
    dockerfiles = {}
    dockerfrom = {}
    print("Docker image tree builder")
    listdockerfiles("/home/jabreu/workspace/python/PythonScripts",dockerfiles)
    print(dockerfiles)
    listafrom(dockerfiles,dockerfrom)
    print(dockerfrom)

if __name__ == "__main__":
    main()