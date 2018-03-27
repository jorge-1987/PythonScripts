#!/usr/bin/env python
import sys

def checkversion(versionstring):
    dot = -1
    startpos = 0
    major = -1
    minor = -1
    fix = -1
    release = -1
    for x in range(0, 2):
        dot = versionstring.find('.')
        #for y in range(startpos, dot):
        if (x == 0):
            major = versionstring[startpos:dot]
            print(major)
            #versionstring[dot] = ""
            versionstring = versionstring.replace('.',' ')
            startpos = dot + 1
        else:
            minor = versionstring[startpos:dot]
            print("else")
            print(minor)
    print("Version String:")
    print(versionstring)

def main(appversion):
    #Check if the version is in correct form
    checkversion(appversion)

main(str(sys.argv[1]))
