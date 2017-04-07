#!/usr/bin/python
#python version 3.x
#Organize files in datacenterhub structure using NDOR directories
#Tested on windwos 10 OS
#author - Ajay
"""
Copy and organize NDOR data in Datacenterhub format

"""
import csv, re, os, fnmatch, shutil, errno, glob
#
def cpdir(src, dest):
    try:
        shutil.copytree(src, dest)
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy2(src, dest)
        else:
            print('Directory not copied. Error: %s' % e)
            
#def maked(dirname):
#            os.mkdir(dirname)
#            print ("created dir " + row[1])
### 
def srchdir(directory):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))
#    matches = []
    dirs = []
    for root, dirnames in os.walk(directory):
        for dirname in dirnames:
#            if dirname == 'plans' :
                print (os.path.join(root,dirname))  # full path of dirs
                dirs.append(dirname)
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches
    return dirs
#    print (matches)

def srchfile(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
    dirs = []
    for root, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
#            if dirname == 'plans' :
#                print (os.path.join(root,dirname))  # full path of dirs
                dirs.append(os.path.join(root,dirname))
        for filename in filenames:
            full_path = os.path.join(root, filename)
#            print(full_path)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return dirs, matches
#    return dirs
    print (matches)

# common processing for categories

def mkdr(root,case,cat):
    dpath = os.path.join(root,case[0],cat)
#    print ('Creating path ', dpath)
    os.makedirs(dpath, mode=0o777, exist_ok=True)
    os.chmod(dpath, 0o777)
    cpdir(line,dpath)
    print(case[1], dpath)

def checkexists(path):
    if os.path.exists(path):
        print ('file already exists -',line )
    
# remove duplicates
#def opencsv():
#    with open('NB.csv', 'r') as f:
#        reader = csv.reader(f)
#        return reader

# source list all the file paths in root directory
# '*' will search and list all files, specific extension can be used as well.
p = 'PHOTOS' #pictures
r = 'MAINTENANCE' #reports
drw = 'PLANS' #drawgins folder
dset = 'DCHUB' #dataid
indir = 'NDOR' # input dir
sdirs,sfiles  = srchfile(indir,'*')
#print ((sfiles))
#with open('inb.csv', 'r') as f:
#    reader = csv.reader(f)
#    count = 0
#    skipped = []
#    for row in reader:
#        for line in source:
#            if re.search(row[1],line):
#                print (row[1],line)
#                count +=1
#                print (count)
#input file contains mapping for caseid and experiment id
with open('input.csv', 'r') as f:
    reader = csv.reader(f)
    count = 0
    skippedcase = []
    skippedfiles = []
    copied = []
    for row in reader: #CSV
        for line in sfiles: #filelist from NDOR
            dirnames = line.split('\\') #fixed for dir names 
            if row[1] in dirnames:
#            if re.search(row[1],line):
#                print (row[1],line)
                #Check for photos #resolve directory check issue.
                if p in dirnames: #check for photos
#                    print('found ',line)
#                if re.search(p , line[5:12],flags=re.I): 
#                    print (p, 'found, Copying now...')
#                    checkexists(line)
                    mkdr(dset,row,'media') #making target dir
#                    print ('file copied', line)
                    count += 1
                    if line not in copied:
                        copied.append(line) #log for copied file
#                #Check for reports
                else: 
                    print ('Photos not found for case', row[1]) # working fine
                if r in dirnames:    # check for reports 
#                if re.search(r , line[5:16],flags=re.I):
#                    checkexists(line)
                    mkdr(dset,row,'reports') # make target dir
#                    print (r, 'found, Copying now...')
                    count += 1
#                    print ('file copied ' + count + ' ', line)
                    if line not in copied:
                        copied.append(line) #log for copied file
#                #Check for drawings
                else: 
                    print ('Reports not found for case', row[1])
                if drw in dirnames:  
#                if re.search(drw , line[5:16],flags=re.I):
#                    checkexists(line)
                    mkdr(dset,row,'drawings')
#                    print (drw, 'found, Copying now...')
                    count += 1
#                    print ('file copied ' + count + ' ', line)
                    if line not in copied:
                        copied.append(line)
                else: 
                    print ('Drawings not found for case', row[1])
            else:
#                print(skipped)
                if row[1] not in sdirs:
                    if row[1] not in skippedcase:
                        skippedcase.append(row[1]) #skipped case ids
#                        print(skipped)
                if line not in (copied ,skippedfiles) :
                    skippedfiles.append(line)
#            continue
        
#                        print(line)
#            continue
    print('end of Copy process', end='\n')
    
    print ('Total files found in NDOR ', len(sfiles),end="\n")
    
    print ('Total case not found in DCHUB', len(skippedcase),end="\n")
#    if (len(skipped) != 0)  :
#        print('list as below -', end='\n')
#        for line in skipped: print(line)
#        print('End of list', end='\n')
#    else: 
#        print('No file skipped', end = '\n')
    
    print ('Total skipped files ', len(set(sfiles) - set(copied)),end="\n")
  
#    if (len(skippedfiles) != 0)  :
#        print('Skipped files as below -')
#        for line in skippedfiles: print(line)
#        print('End of list',end='\n')
#    else: 
#        print('No file skipped',end='\n')
        
    print ('Total Copied in DCHUB', len(copied),end="\n")    
#    if (len(copied) != 0) :
#        print('Copied files as below -',end='\n')
#        for line in copied: print(line)
#        print('End of list', end='\n')
#    else: 
#        print('No file skipped',end='\n')
        
#    print ('Total found in NDOR ', len(sfiles),end="\n")
#    print ('Total Copied in DCHUB', len(copied),end="\n")
#    print ('Total skipped ', len(skippedfiles),end="\n")
#        else: 
##                print ('Not found')
#                continue
##print ('total copied',count)
###for line in file:
##    if line in caseno: print('match', line)
##    for line in source:
##        if caseno in line
##    else: print('no match')

#i = 1
#for line in source:
#    print (i, line)
#    i += 1