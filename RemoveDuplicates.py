#!/usr/bin/env python
#This is my first Python Script, I dont know how #!/usr/bin... affects in Windows
import os
import sys
import hashlib

SourceListDic = {}
DuplicatesListDic = {}
DuplicatesListO = []
DuplicatesListD = []

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
            #print(os.path.join(root, file))
            SourceListDic[str(os.path.join(root, file))] = md5(os.path.join(root, file))
             
#Based from an answer in Stackoverflow
#http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
def ListaDuplicatesGen(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            #print(os.path.join(root, file))
            DuplicatesListDic[str(os.path.join(root, file))] = md5(os.path.join(root, file))
            
def SearchDuplicates(Source,Duplicates):
        #List files and make their md5 hash
    ListaSourceGen(Source)
    ListaDuplicatesGen(Duplicates)
    
    #Search for duplicates in the md5 of the ListaDuplicatesGen and put the file string in DuplicatesList
    SourceDirLen = len(SourceListDic.keys())
    DuplicatesDirLen = len(DuplicatesListDic.keys())
    print "El directorio Origen tiene: " + str(len(SourceListDic.keys())) + " Archivos"
    print "El directorio para buscar duplicados tiene: " + str(len(DuplicatesListDic.keys())) + " Archivos"
    print "" 
    
    for x in range(0, SourceDirLen):
        #print str(x)
        for y in range(0, DuplicatesDirLen):
            if (SourceListDic[SourceListDic.keys()[x]] == DuplicatesListDic[DuplicatesListDic.keys()[y]]):
                #print "Son iguales."
                DuplicatesListO.append(SourceListDic.keys()[x])
                DuplicatesListD.append(DuplicatesListDic.keys()[y])
                #DuplicatesList.append("x")
                
def DuplicatesList():
    Duplicateslen = len(DuplicatesListD)
    if (Duplicateslen == 0):
        print "No existen archivos duplicados del directorio origen en el directorio destino"
        print "" 
    else: 
        print "En la carpeta destino se encontraron los siguientes archivos que ya existen en la carpeta de origen: "
        print "" 
        for z in range(0, Duplicateslen):
            print "Archivo origen: "
            print DuplicatesListO[z]
            print "Duplicado en destino como: "
            print DuplicatesListD[z]
            print "" 
        #print SourceListDic
    
def DeleteDuplicates():
    print "Se eliminaran los duplicados."
    count = 0
    Duplicateslen = len(DuplicatesListD)
    for z in range(0, Duplicateslen):
        if (os.path.isfile(DuplicatesListD[z])):
            os.remove(DuplicatesListD[z])
            count = count+1
            
    print "Se eliminaron: " + str(count) + " archivos." 
    print "" 
    #print SourceListDic
    
    
def main(folderSource,folderDuplicates):
    print "Bienvenido a RemoveDuplicates."
    print "" 
    #Ask if the user wants to print the list, or delete the duplicates.
    opt = 9
    while (opt != 0):
        print '1) Buscar y listar duplicados.'
        print '2) Buscar, listar y Eliminar duplicados.'
        print '3) Buscar y Eliminar duplicados.'
        print '0) Salir.'
        print "" 
        opt = input("Su seleccion: ")
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
