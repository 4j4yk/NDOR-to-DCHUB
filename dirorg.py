#!/usr/bin/python
#python version 3.x
#Organize files in datacenterhub structure using NDOR directories
#Tested on windwos 10 OS
#author - Ajay
"""
Copy and organize NDOR data in Datacenterhub format

"""
import csv, re, os, fnmatch, shutil, errno
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
def srchfile(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))

    matches = []
#    dir = []
    for root, dirnames, filenames in os.walk(directory):
#        for dirname in dirnames:
#            print (dirname)
#            dir.append(dirname)
        for filename in filenames:
            full_path = os.path.join(root, filename)
            if fnmatch.filter([full_path], pattern):
                matches.append(os.path.join(root, filename))
    return matches
#    return dir
#    print (matches)

# common processing for categories

def mkdr(root,case,cat):
    dpath = os.path.join(root,case,cat)
    print ('Creating path ', dpath)
    os.makedirs(dpath, mode=0o777, exist_ok=True)
    os.chmod(dpath, 0o777)
    cpdir(line,dpath)

# source list all the file paths in root directory
# '*' will search and list all files, specific extension can be used as well.
p = 'PHOTOS' #pictures
r = 'MAINTENANCE' #reports
drw = 'PLANS' #drawgins folder
dset = '1582' #dataid
indir = 'test1' # input dir
source = srchfile(indir,'*')

#input file contains mapping for caseid and experiment id
with open('inb.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        for line in source:
            if re.search(row[1],line):
                #Check for photos
                if re.search(p , line):
                    mkdr(dset,row[0],'media')
                    print ('file copied', line)
                #Check for reports
                if re.search(r , line):
                    mkdr(dset,row[0],'reports')
                    print ('file copied', line)
                #Check for drawings
                if re.search(drw , line):
                    mkdr(dset,row[0],'drawings')
                    print ('file copied', line)
            else: continue

##for line in file:
#    if line in caseno: print('match', line)
#    for line in source:
#        if caseno in line
#    else: print('no match')