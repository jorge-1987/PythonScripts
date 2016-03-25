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
    
#Based from an answer in Stackoverflow
#http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
def ListaSourceGen(dir):
    Sourcelist = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            SourceListDic[str(os.path.join(root, file))] = md5(os.path.join(root, file))
             
#Based from an answer in Stackoverflow
#http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
def ListaDuplicatesGen(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            DuplicatesListDic[str(os.path.join(root, file))] = md5(os.path.join(root, file))
            
def SearchDuplicates(Source,Duplicates):
        #List files and make their md5 hash
    ListaSourceGen(Source)
    ListaDuplicatesGen(Duplicates)
    
    #Search for duplicates in the md5 of the ListaDuplicatesGen and put the file string in DuplicatesList
    SourceDirLen = len(SourceListDic.keys())
    DuplicatesDirLen = len(DuplicatesListDic.keys())
    print "The origin folder has: " + str(SourceDirLen) + " files"
    print "The folder to search duplicated files has: " + str(DuplicatesDirLen) + " files"
    print "" 
    
    for x in range(0, SourceDirLen):
        if (Silent == 0):
            print str(x) + "/" + str(SourceDirLen)
        for y in range(0, DuplicatesDirLen):
            if (SourceListDic[SourceListDic.keys()[x]] == DuplicatesListDic[DuplicatesListDic.keys()[y]]):
                DuplicatesListO.append(SourceListDic.keys()[x])
                DuplicatesListD.append(DuplicatesListDic.keys()[y])

def DuplicatesList():
    Duplicateslen = len(DuplicatesListD)
    if (Duplicateslen == 0):
        print "There is no duplicated files in the folder."
        print "" 
    else: 
        print "In the destination folder there is some duplicated files as list below: "
        print "" 
        for z in range(0, Duplicateslen):
            print "Origin file: "
            print DuplicatesListO[z]
            print "Duplicated in destiny folder as: "
            print DuplicatesListD[z]
            print "" 

    
def DeleteDuplicates():
    print "Deleted duplicated files."
    count = 0
    Duplicateslen = len(DuplicatesListD)
    for z in range(0, Duplicateslen):
        if (os.path.isfile(DuplicatesListD[z])):
            os.remove(DuplicatesListD[z])
            count = count+1
            
    print "Deleted : " + str(count) + " files." 
    print "" 

    
def main(folderSource,folderDuplicates):
    print "Welcome to RemoveDuplicates."
    print "" 
    #Ask if the user wants to print the list, or delete the duplicates.
    opt = 9
    while (opt != 0):
        print '1) Find and List duplicated files.'
        print '2) Find, List and Delete duplicated files.'
        print '3) Find and Delete duplicated files.'
        print '0) Exit.'
        print "" 
        opt = input("Input your choice: ")
        print ""
        if (opt==1):
            SearchDuplicates(folderSource,folderDuplicates)
            DuplicatesList()
        elif (opt==2):
            SearchDuplicates(folderSource,folderDuplicates)
            DuplicatesList()
            DeleteDuplicates()
        elif (opt==3):
            SearchDuplicates(folderSource,folderDuplicates)
            DeleteDuplicates()
    
    print "" 
    print "Good Bye!"

main(str(sys.argv[1]),str(sys.argv[2]))
