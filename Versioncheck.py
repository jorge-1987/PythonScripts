#!/usr/bin/env python
import sys

def checkversion(versionstring):
    dot = -1
    startpos = 0
    major = -1
    minor = -1
    fix = -1
    release = -1
#    for x in range(0, 2):
    dot = versionstring.find('.')
        #for y in range(startpos, dot):
#        if (x == 0):
    try:
        major = int(versionstring[startpos:dot])
    except:
        major = versionstring[startpos:dot]
        print(major + " not a major version number.")
        exit(1)

    print("Major ok:")
    print(major)

    versionstring = versionstring.replace('.',' ',1)
    startpos = dot + 1
#        else:
#    print("Version String:")
#    print(versionstring)
    dot = versionstring.find('.')
    try:
        minor = int(versionstring[startpos:dot])
    except:
        minor = versionstring[startpos:dot]
        print(minor + " not a minor version number.")
        exit(1)

    print("Minor ok:")
    print(minor)

#    dot = versionstring.find('.')            
    startpos = dot + 1
    dash = versionstring.find('-')
#    print("dash pos:")
#    print(dash)
#    print(startpos)
    versionstring = versionstring.replace('.',' ',1)
    endstr = len(versionstring)
    if (dash > 1):
        try:
            fix = int(versionstring[startpos:dash])
        except:
            fix = versionstring[startpos:dash]
            print(fix + " not a fix version number.")
            exit(1)

        print("Fix ok:")
        print(fix)
        startpos = dash + 1
        release = versionstring[startpos:endstr]
        print("Release:")
        print(release)
    else:
        try:
            fix = int(versionstring[startpos:endstr])
        except:
            fix = versionstring[startpos:endstr]
            print(fix + " not a fix version number.")
            exit(1)

        print("Fix:")
        print(fix)

    print("Version String at end:")
    print(versionstring)

def main(appversion):
    #Check if the version is in correct form
    print("Version String original:")
    print(appversion)

    checkversion(appversion)

main(str(sys.argv[1]))
