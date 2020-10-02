#!/usr/bin/env python
import os

#list all the Dockerfiles
def listdockerfiles(path,dockerdict):
    fromlst = []
    fullpath = ""
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.startswith("Dockerfile"):
#                print(os.path.join(root, file))
                fullpath = os.path.join(root, file)
                dockerdict[fullpath] = fromlst

#Get all the FROMs per dockerfile

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
    print("Docker image tree builder")
    listdockerfiles("/home/jabreu/workspace/php/easyquizgame/mysql",dockerfiles)
    print(dockerfiles)


if __name__ == "__main__":
    main()