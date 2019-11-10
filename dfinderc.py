#!/usr/bin/env python
import os
import sys
import hashlib
import getopt

import multiprocessing
import time

SourceListDic = {}
DuplicatesListDic = {}


Delete = False


def usage():
  print("Find duplicates files between an origin and a destination where the duplicates should NOT be using concurrents")
  print("DeplicatesFinder.py -o /home/joe/importantfilesdirectory -d /tmp/mixoffilestobedeleted")

#From Stackoverflow
#http://stackoverflow.com/questions/3431825/generating-a-md5-checksum-of-a-file
def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


def ListaLevel1(Dir,Lista):
	for dirName, subdirList, fileList in os.walk(Dir):
		#print('Found directory: %s' % dirName)
		for fname in fileList:
			#print str(dirName)+str(fname)
			Lista[str(dirName)+"/"+str(fname)] = md5(str(dirName)+"/"+str(fname))
		if len(subdirList) > 0:
			del subdirList[:]

#FUNCION CONCURRENTE
def SearchDuplicatesC(X):
    if str(X).endswith('0'):
      print(str(X))
    SourceDirLen = len(SourceListDic.keys())
    DuplicatesDirLen = len(DuplicatesListDic.keys())
    for y in range(0, DuplicatesDirLen):
      if (SourceListDic[list(SourceListDic.keys())[X]] == DuplicatesListDic[list(DuplicatesListDic.keys())[y]]):
        print("Duplicado")
        print(str(X))
        print(str(list(SourceListDic.keys())[X]))
        if Delete:
          if (os.path.isfile(str(list(DuplicatesListDic.keys())[y]))):
            print("Deleting:")
            print(str(list(DuplicatesListDic.keys())[y]))
            os.remove(str(list(DuplicatesListDic.keys())[y]))



def SearchDuplicates():
    #List files and make their md5 hash
    #Search for duplicates in the md5 of the ListaDuplicatesGen and put the file string in DuplicatesList
    SourceDirLen = len(SourceListDic.keys())
    DuplicatesDirLen = len(DuplicatesListDic.keys())
    print ("The origin folder has: " + str(SourceDirLen) + " files")
    print ("The folder to search duplicated files has: " + str(DuplicatesDirLen) + " files")
    print (" ") 
    with multiprocessing.Pool() as pool:
      pool.map(SearchDuplicatesC, range(0, SourceDirLen))

def DuplicatesList():
    Duplicateslen = len(DuplicatesListD)
    if (Duplicateslen == 0):
        print ("There is no duplicated files in the folder.")
        print ("")
    else: 
        print ("In the destination folder there is some duplicated files as list below: ")
        print ("")
        for z in range(0, Duplicateslen):
            print ("Origin file: ")
            print (DuplicatesListO[z])
            print ("Duplicated in destiny folder as: ")
            print (DuplicatesListD[z])
            print ("")
def main():
    commflag = False
    comm = ""
    global Delete

    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:d:")
    except getopt.GetoptError as err:
        # print help information and exit:
        print (str(err))  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)

    origin = ""
    duplicates = ""

    for o, a in opts:
        if o == "-o":
            origin = a
        elif o in ("-h"):
            usage()
            sys.exit()
        elif o == "-d":
            duplicates = a
        else:
            assert False, "unhandled option"

    if (origin == ""):
      print("A valid Original files directory not set with -o")
      usage()
      sys.exit(2)

    if (duplicates == ""):
      print("A valid Duplicated files directory not set with -d")
      usage()
      sys.exit(2)

    print("Starting the search")
    print("Origin files directory: " + origin)
    print("Duplicated files directory: " + duplicates)

    print("What to do with the duplicates found?")
    print("Enter L to list them and send them to a Logfile, D to delete them, E to exit")

    while commflag == False:
      comm = input("L, D or E? : ")
      if (comm == "E"):
        commflag = True
        print("Bye bye!")
      if (comm == "L"):
        print("List:")
        ListaLevel1(origin,SourceListDic)
        ListaLevel1(duplicates,DuplicatesListDic)
        SearchDuplicates()
        print("List finished!")
      if (comm == "D"):
        commflag = True
        Delete = True
        print("Search and Destroy:")
        ListaLevel1(origin,SourceListDic)
        ListaLevel1(duplicates,DuplicatesListDic)
        SearchDuplicates()
        print("Deleting finished!")



if __name__ == "__main__":
    main()
