# NDOR to DCHub data upload
NDOR FTP pull program. Reorganizes NDOR Bridge Data into DataCenterHub's directory structure in order to be uploaded onto their system.

# System Requirements
Python - Version 3.x.x
PHP - Version 5.6.x

# Pull instructions
To install the directory package, run the following command:

    $ git clone https://github.com/akhampariya/ndorftp.git

# List of Programs and Files
Programs:
1. dirorg.py - Python3 program which sorts the NDOR Bridge Data into DataCenterHub's format
2. uploadNDORData.php - PHP program intended to upload all sorted NDOR Bridge data files onto DataCenterHub
3. testPHPFTP - original program idea to gather and sort files directly from NDOR Bridge Data's FTP server

Major Files:
1. DCHUB/ - Directory containing sorted output data from dirorg.py
2. NDOR/ - Directory containing unsorted input data for dirorg.py
3. tests/ - Directory containing input data for uploadNDORData.php


# To-do list
1. Testing dirorg.py program with bulk NDOR data. In progress... taking hours
2. SFTP upload - going to be sent for testing, recursive upload from local desktop has been tested for some directories.
3. Test uploadNDORData.php on DCHub Dev platform once sample data is SFTPed.
4. Keep a count of all files found in directories and match them after copying into destination.    - Fixed.
5. Review and enhance error handling for failures.  - In progress
6. Identify and log such file which are not associated with any case id. - Fixed partially.
7. Improve Regex logic to check directory name from starting position.         - Fixed, regex removed and exact directory name comparison in place.
8. Python program has been updated to show size of input directory and start/end time.
9. Route the log lists to text files.

# Potential issues might occur
1. Directory names may contain characters other than number and alphabets, which may cause problems. Testing is required. - In progress
2. There are some files which are not assiciated with experiments ID, what should be done with such files? - Partially fixed.
3. There are files which are under removed from inventory files, what should be done with that? - Ignored in the program but logged in skipped files.

# Meeting notes
All meeting notes are placed into the UNO box folder and can be accessed via below link - 
https://unomaha.box.com/v/weeklymeetings

For any queries contact contributers of the repository.
