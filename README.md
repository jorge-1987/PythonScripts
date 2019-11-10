# PythonScripts

## Scripts in Python for daily work:

## RemoveDuplicates.py
Script for finding duplicated files between two folders, the first one as the origin of the files, and the second one to search for duplicates in there.
### Use:
RemoveDuplicates.py OriginFolder FolderWithSuspectedDuplicatedFiles

## DuplicatesFinder.py
Script for finding duplicated files between two folders, the first one as the origin of the files, and the second one to search for duplicates in there.
### Use:
Find duplicates files between an origin, and a destination where the duplicates should NOT be:
python3 DeplicatesFinder.py -o /home/joe/importantfilesdirectory -d /tmp/mixoffilestobedeleted

## dfinderc.py
Script for finding duplicated files between two folders, the first one as the origin of the files, and the second one to search for duplicates in there. This version uses multiprocessing to compare directories with big amounts of files. You could select to list them and store the duplicates in a log file, or delete them everytime that a duplicate is found.
### Use:
Find duplicates files between an origin, and a destination where the duplicates should NOT be:
python3 dfinderc.py -o /home/joe/importantfilesdirectory -d /tmp/mixoffilestobedeleted

## ApacheDiffReload.py
This scripts was created in the context that you have two apache servers, on does an rsync in the other one, but if the rsync updates a configuration file in the second server, apache needs to reload to take effect, so with this script, you pass as parameters the path of the configuration file that rsync updates, and a path where you have a backup of the file. If there is a difference between the files, reloads the apache, and copy the new config file to the backup path, so in that way now the configuration files are in sync and reloaded.
### Use:
/scripts/ApacheDiffReload.py /etc/apache2/sites-enabled/Default /backup/Default.backup
