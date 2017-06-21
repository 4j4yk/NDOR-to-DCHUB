# Introduction
This repository is part of Bridging Big Data project. This set of programs works for directory re-structure and upload to DataCenterhub platform.

# Why ? 

The Nebraska Department of Roads has been maintaining reports, drawings and other medial files on FTP server and National Bridge Inventory also has bridge data in csv files. We are collating for the data from both and uploading it on DataCenterHub platform. This process also requires converting the NDOR directory structure to DataCenterHub directory structure. Once the re-structring is complete, we can SFTP this data to DataCenterHub SFTP location and they can run the upload script to upload and associate these files with specefic case. All the Structure details and relate drawings, reports and media files are available on this in central platform now. 

# How ? 
To achieve this requirement - 
* we have downloaded NDOR FTP dump to local machine where we will perform direcotry re-structruing. 
* Once re-structure is complete, we will SFTP all the directories to DataCenterHub location.
* DataCenterHub POC will check and run upload script and place them in appropriate folders as well as associate them with respective record structures. 

# Program Setup
## System Requirements
Python - Version 3.x.x
PHP - Version 5.6.x

## Pull instructions
To install the directory package, run the following command:

    $ git clone https://github.com/akhampariya/ndorftp.git

## List of Programs and Files
Programs:
1. dirorg.py - Python3 program which sorts the NDOR Bridge Data into DataCenterHub's format
2. uploadNDORData.php - PHP program intended to upload all sorted NDOR Bridge data files onto DataCenterHub
3. testPHPFTP - original program idea to gather and sort files directly from NDOR Bridge Data's FTP server

Major Files:
1. DCHUB/ - Directory containing sorted output data from dirorg.py
2. NDOR/ - Directory containing unsorted input data for dirorg.py
3. tests/ - Directory containing input data for uploadNDORData.php

# Current Status
- [x] NDOR FTP data transfer to local machine.
- [x] Restructure the NDOR direcotries to DataCenterHub directory structure. 
- [x] SFTP all the directories to DataCenterHub.
- [x] Upload to respective DataCenterHub experiment locations.

# Links 
More Information - [BridgingBigData](https://bridgingbigdata.github.io)
WorkShop - [BBD Workshop](http://engineering.unl.edu/bridging-big-data-workshop/)

# Meeting notes
All meeting notes are placed into the UNO box folder and can be accessed [here](https://unomaha.box.com/v/weeklymeetings).

*For any queries contact contributers of the repository.*
