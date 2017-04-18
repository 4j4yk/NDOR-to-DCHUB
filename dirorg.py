#!/usr/bin/python
#python version 3.x
#Organize files in datacenterhub structure using NDOR directories
#Tested on windwos 10 OS
#author - Ajay
"""
Copy and organize NDOR data in Datacenterhub format

"""
import csv, re, os, fnmatch, shutil, errno, glob, time,json
from datetime import timedelta
from os.path import join, getsize, isfile, isdir, splitext

def GetFolderSize(path):
    TotalSize = 0
    for item in os.walk(path):
        for file in item[2]:
            try:
                TotalSize = TotalSize + getsize(join(item[0], file))
            except:
                print("error with file:  " + join(item[0], file))
    return TotalSize

def cpdir(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        if e.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)         

def srchfile(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    dirs = []
    for root, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
                dirs.append(os.path.join(root,dirname))
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return dirs, matches
# common processing for categories

def make_dir(root,case,cat,spath):
    dpath = os.path.join(root,case[0],cat)
    if os.path.isfile(dpath):
        print ('file already exists -',dpath)
    else:
        os.makedirs(dpath, mode=0o777, exist_ok=True)
        os.chmod(dpath, 0o777)
        cpdir(spath,dpath)      

def checkexists(path):
    if os.path.exists(path):
        print ('file already exists -',line )
    
# source list all the file paths in root directory
# '*' will search and list all files, specific extension can be used as well.
prog_start_time = time.monotonic()
print('Program started -', time.ctime())
# Required for input and search
img_dir = 'PHOTOS'          #pictures
rpt_dir = 'MAINTENANCE'     #reports
plan_dir = 'PLANS'          #drawgins folder
in_dir = 'NDOR'              #input dir
in_csv = 'input.csv'
print ('Calculating input directory size ....', end='\n')
print('Input dir size in GB->',float(GetFolderSize(in_dir)) /1024 /1024 /1024, end = '\n')
#required for output
out_dir= 'DC1'              #output dir
op_media    = 'media'       #output dir media
op_reports  = 'reports'     #output dir reports
op_drawings = 'drawings'    #output dir drawings
sdirs,sfiles = srchfile(in_dir,'*') # assign lists to variables
tsfile = len(sfiles)
log_f1 = open('notcopied.txt', 'w')
log_copied = open('copied.txt', 'w')
log_f2 = open('nocasefound.txt', 'w')
filelist = open('ndorfilelist.txt', 'w')
for files in sfiles: print (files, file = filelist)
filelist.close()
with open(in_csv, 'r') as f:   #contain DCHUB ID and experiment/case id
    reader = csv.reader(f)
    csv_list = list(reader)
    csv_list.sort()
    file_list = list(sfiles)
    file_list.sort()
    f.close()
    count = 0
    skippedcase  = []
    copied       = []
    for row in csv_list: #CSV
        for line in file_list:                  #filelist from NDOR
            dirnames = line.split('\\')
            macdirnames = line.split('/')       #break into dirs 

            if row[1] in dirnames or row[1] in macdirnames:
                if img_dir in dirnames or img_dir in macdirnames: #check for photos
                    make_dir(out_dir, row, op_media, line) #making target dir and copy
                    count += 1
                    if line not in copied:
                        copied.append(line) #log for copied file
                        print(line, file = log_copied)
                        file_list = set(file_list) - set(copied)
                else: 
                    print ('Photos not found for case', row, file = log_f2)
                if rpt_dir in dirnames or rpt_dir in macdirnames:    # check for reports 
                    make_dir(out_dir, row, op_reports,line) # make target dir
                    count += 1

                    if line not in copied:
                        copied.append(line) #log for copied file
                        print(line, file = log_copied)
                        file_list = set(file_list) - set(copied)
                else: 
                    print ('Reports not found for case', row, file = log_f2)
                if plan_dir in dirnames or plan_dir in macdirnames:  
                    make_dir(out_dir, row, op_drawings,line)
                    count += 1
                    if line not in copied:
                        copied.append(line)
                        print(line, file = log_copied)
                        file_list = set(file_list) - set(copied)
                else: 
                    print ('not found for case', row, file = log_f2)
                    
            else:
                if row[1] not in sdirs:
                    if row[1] not in skippedcase:
                        skippedcase.append(row[1]) #skipped case ids

    print ('end of Copy process', end='\n')
    print ('Total files found in NDOR ->', tsfile ,end="\n")
    print ('Total Copied in '+ out_dir + '->' , len(copied),end="\n")        
    print ('Total case not found in DCHUB CSV ->', len(skippedcase),end="\n")
    skip_list = set(file_list) - set(copied)
    print ('Total skipped files ->', len(skip_list),end="\n")
    for f in skip_list: print (f, file = log_f1)       
   
# calculate time taken 
log_f1.close()
log_f2.close()
log_copied.close()
prog_end_time = time.monotonic()
print ('Program ended - ', time.ctime())
print ('Program execution time ->', timedelta(seconds=prog_end_time - prog_start_time))