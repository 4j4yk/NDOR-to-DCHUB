# ndorftp
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
