# NDOR to DCHub data upload
NDOR FTP pull program. Reorganizes NDOR Bridge Data into DataCenterHub's directory structure in order to be uploaded onto their system.

# System Requirements
Python - Version 3.x.x
PHP - Version 5.6.x

# Pull instructions
To install the directory package, run the following command:

git clone https://github.com/akhampariya/ndorftp.git

# List of Programs and Files
Programs:
1. dirorg.py - Python3 program which sorts the NDOR Bridge Data into DataCenterHub's format
2. uploadNDORData.php - PHP program intended to upload all sorted NDOR Bridge data files onto DataCenterHub
3. testPHPFTP - original program idea to gather and sort files directly from NDOR Bridge Data's FTP server

Major Files:
1. 1582/ - Directory containing sorted output data from dirorg.py
2. test1/ - Directory containing unsorted input data for dirorg.py
3. tests/ - Directory containing input data for uploadNDORData.php


# To-do list

1. Testing dirorg.py program with bulk NDOR data.
2. SFTP upload
3. Test uploadNDORData.php on DCHub Dev platform once sample data is SFTPed.
4. Keep a count of all files found in directories and match them after copying into destination.
5. Review and enhance error handling for failures.  
6. Identify and log such file which are not associated with any case id.
7. Improve Regex logic to check dir name from starting position.

# Potential issues might occur
1. Direcotry names may contain characters other than number and alphabets, which may cause problems,testing is required.
2. There are some files which are not assiciated with experiments ID, what should be done with such files?
3. There are files which are under removed from inventory files, what should be done with that?


For any quries contact contributers of the repository.
