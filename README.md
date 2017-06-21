# Introduction
This repository is part of the [Bridging Big Data project](https://bridgingbigdata.github.io) sponsored by NSF. The included scripts re-structure file directories from a Nebraska Department of Roads (NDOR) Bridge Inventory Management system for upload to the [DataCenterHub] (https://datacenterhub.org) platform.

# Why? 

NDOR has been maintaining reports, drawings and other media files for all Nebraska bridges using a local Bridge Management system. This dataset was previously shared with researchers using an FTP server with no metadata and minimal search, query and retreival functions. To improve access to this dataset for NDOR and researchers nationwide, we have developed a set of programs for its curation and transition to a NSF DIBBS platform. Each file related to bridge health is also alinged and annotated with bridge inspection records submitted annually by NDOR to the National Bridge Inventory. This process  requires converting the NDOR bridge management system directory structure to DataCenterHub directory structure. 

# How? 
To achieve this requirement we undertake the following steps
* Downloaded NDOR FTP accessible files to a local machine
* Initialize Datacenterhub with NBI data to obtain unique caseIDs for each bridge
* Perform local directory restructuring to align bridge structures with Datacenterhub case IDs
* Upload restructured directories to DataCenterHub
* DataCenterHub POC will check and run upload script and place them in appropriate folders as well as associate them with separate record structures. 

# Program Setup
## System Requirements
Python - Version 3.x.x
PHP - Version 5.6.x

## Pull instructions
To install the directory package, run the following command:

    $ git clone https://github.com/akhampariya/ndorftp.git

## List of Programs and Files
Programs:
1. dirorg.py - the Python3 program which sorts the NDOR Bridge Data into DataCenterHub's format
2. uploadNDORData.php - PHP program intended to upload all sorted NDOR Bridge data files onto DataCenterHub
3. testPHPFTP - original program idea to gather and sort files directly from NDOR Bridge Data's FTP server

Major Files:
1. DCHUB/ - Directory containing sorted output data from dirorg.py
2. NDOR/ - Directory containing unsorted input data for dirorg.py
3. tests/ - Directory containing input data for uploadNDORData.php

## Run 

Place all the files in a folder and point the inputDir and outputDir in the program correctly.

$ python3 dirorg.py

It will produce restructured directories in the outputDir folder. These now can be uploaded to DataCenterHub SFTP location.

# Current Status
- [x] NDOR FTP data transfer to the local machine.
- [x] Restructure the NDOR directories to DataCenterHub directory structure. 
- [x] SFTP all the directories to DataCenterHub.
- [x] Upload to respective DataCenterHub experiment locations.

# Links 
More Information - [BridgingBigData](https://bridgingbigdata.github.io)
WorkShop - [BBD Workshop](http://engineering.unl.edu/bridging-big-data-workshop/)

# Meeting notes
All meeting notes are placed into the UNO box folder and can be accessed [here](https://unomaha.box.com/v/weeklymeetings).

*For any queries contact contributors of the repository.*
