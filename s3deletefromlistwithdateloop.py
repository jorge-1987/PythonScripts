#!/usr/bin/env python
import os
import sys
import getopt
import boto3
import botocore
import datetime

def usage():
	print("Delete a list of files from an S3 bucket path only knowing the year and the month")
	print("filedeleter.py -b bucketname -f listadearchivos.txt -p raw/sftp/ce/epes/epes/2019")

def main():
	bucket = ""
	filelist = ""
	path = ""
	now = datetime.datetime.now()
	s3 = boto3.resource("s3")
	print("Files are going to be deleted")

	try:
		opts, args = getopt.getopt(sys.argv[1:], "b:f:p:")
	except getopt.GetoptError as err:
        # print help information and exit:
		print (str(err))  # will print something like "option -a not recognized"
		usage()
		sys.exit(2)


	for o, a in opts:
		if o == "-b":
			bucket = a
		elif o in ("-f"):
			filelist = a
		elif o in ("-p"):
			path = a


	if (bucket == ""):
		print("A valid Bucket not set with -b")
		usage()
		sys.exit(2)

	if (filelist == ""):
		print("A valid files list not set with -f")
		usage()
		sys.exit(2)

	if (path == ""):
		print("A valid path not set with -p")
		usage()
		sys.exit(2)

	print(bucket)
	print(filelist)
	print("Starting list:")

	s3 = boto3.resource("s3")

	file = open(filelist, "r")
	timestamp = str(now.year) +'-'+ str(now.month) +'-'+ str(now.day) +'-'+ str(now.hour) +'-'+ str(now.minute) +'-'+ str(now.second)
	notable = "notabletodelete."+timestamp+".log"
	fnot = open(notable, 'w')

	for f in file:
		for y in range(31):
			fullpath = path+"/"+(y+1).zfill(2)+"/"+f.strip('\n')
			#print(fullpath)
			obj = s3.Object(bucket, fullpath)
			try:
				obj.load()
			except botocore.exceptions.ClientError as e:
				if e.response['Error']['Code'] == "404":
					#print("File does not exists-"+fullpath)
					fnot.write(fullpath+'\n')
				else:
					# Something else has gone wrong.
					raise
			else:
				# The object does exist.
				obj.delete()
				print("Deleted-"+fullpath)

	fnot.close()
	file.close()
	print("Finished list.")

if __name__ == "__main__":
    main()
