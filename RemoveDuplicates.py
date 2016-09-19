#!/usr/bin/env python
import os
import sys
import hashlib

SourceListDic = {}
DuplicatesListDic = {}
DuplicatesListO = []
DuplicatesListD = []
Silent = 0

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
			Lista[(str(dirName)+"\\"+str(fname))] = md5((str(dirName)+"\\"+str(fname)))
		if len(subdirList) > 0:
			del subdirList[:]
			

def SearchDuplicates():
	#List files and make their md5 hash
	#Search for duplicates in the md5 of the ListaDuplicatesGen and put the file string in DuplicatesList
    SourceDirLen = len(SourceListDic.keys())
    DuplicatesDirLen = len(DuplicatesListDic.keys())
    print ("The origin folder has: " + str(SourceDirLen) + " files")
    print ("The folder to search duplicated files has: " + str(DuplicatesDirLen) + " files")
    print (" ") 
    for x in range(0, SourceDirLen):
        if (Silent == 0):
            print (str(x) + "/" + str(SourceDirLen))
        for y in range(0, DuplicatesDirLen):
            if (SourceListDic[SourceListDic.keys()[x]] == DuplicatesListDic[DuplicatesListDic.keys()[y]]):
                DuplicatesListO.append(SourceListDic.keys()[x])
                DuplicatesListD.append(DuplicatesListDic.keys()[y])

def DuplicatesList():
    Duplicateslen = len(DuplicatesListD)
    if (Duplicateslen == 0):
        print ("There is no duplicated files in the folder.")
        print (" ")
    else: 
        print ("In the destination folder there is some duplicated files as list below: ")
        print (" ") 
        for z in range(0, Duplicateslen):
            print ("Origin file: ")
            print (DuplicatesListO[z])
            print ("Duplicated in destiny folder as: ")
            print (DuplicatesListD[z])
            print (" ")

def DeleteDuplicates():
    print ("Deleted duplicated files.")
    count = 0
    Duplicateslen = len(DuplicatesListD)
    for z in range(0, Duplicateslen):
        if (os.path.isfile(DuplicatesListD[z])):
            os.remove(DuplicatesListD[z])
            count = count+1
            
    print ("Deleted : " + str(count) + " files.") 
    print (" ")

def main(folderSource,folderDuplicates):
    print ("Welcome to RemoveDuplicates.")
    print (" ")
	#Ask if the user wants to print the list, or delete the duplicates, etc...
    opt = 9
    while (opt != 0):
        print ('1) Find, List, and delete duplicated files.')
        print ('0) Exit.')
        print (" ")
        opt = input("Input your choice: ")
        print (" ")
        if (opt == 1): 
			ListaLevel1(folderSource, SourceListDic)
			ListaLevel1(folderDuplicates, DuplicatesListDic)
			SearchDuplicates()
			DuplicatesList()
			DeleteDuplicates()

	print(" ")
    print("Good Bye!")

main(str(sys.argv[1]), str(sys.argv[2]))
