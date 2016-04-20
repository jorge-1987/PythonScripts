# PythonScripts

#Scripts in Python for daily work:

#RemoveDuplicates.py
Script for finding duplicated files between two folders, the first one as the origin of the files, and the second one to search for duplicates in there.
Use:
RemoveDuplicates.py OriginFolder FolderWithSuspectedDuplicatedFiles

#ApacheDiffReload.py
This scripts was created in the context that you have two apache servers, on does an rsync in the other one, but if the rsync updates a configuration file in the second server, apache needs to reload to take effect, so with this script, you pass as parameters the path of the configuration file that rsync updates, and a path where you have a backup of the file. If there is a difference between the files, reloads the apache, and copy the new config file to the backup path, so in that way now the configuration files are in sync and reloaded.
Use:
/scripts/ApacheDiffReload.py /etc/apache2/sites-enabled/Default /backup/Default.backup
