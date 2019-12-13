#!/usr/bin/env python
import os
import sys
import getopt
import boto3
import botocore

def usage():
	print("Delete a list of files from an S3 bucket path")
	print("filedeleter.py -b bucketname -f listadearchivos.txt")

def main():
	bucket = ""
	filelist = ""
	s3 = boto3.resource("s3")
	print("Files are going to be deleted")

	try:
		opts, args = getopt.getopt(sys.argv[1:], "b:f:")
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


	if (bucket == ""):
		print("A valid Bucket not set with -b")
		usage()
		sys.exit(2)

	if (filelist == ""):
		print("A valid files list not set with -f")
		usage()
		sys.exit(2)

	print(bucket)
	print(filelist)
	print("Starting list:")

	s3 = boto3.resource("s3")

	file = open(filelist, "r")
	fnot = open('notabletodelete.log', 'w')

	for x in file:
		obj = s3.Object(bucket, x.strip('\n'))
		#print(x.strip('\n'))
		try:
			obj.load()
		except botocore.exceptions.ClientError as e:
			if e.response['Error']['Code'] == "404":
				print("File does not exists-"+x.strip('\n'))
				fnot.write(x)
			else:
				# Something else has gone wrong.
				raise
		else:
			# The object does exist.
			obj.delete()
			print("Deleted-"+x.strip('\n'))

	fnot.close()
	file.close()
	print("Finished list.")

if __name__ == "__main__":
    main()
