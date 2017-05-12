#!/usr/bin/python
#python version 3.x
#CSV file compare and produce matching case id mapping 
#Tested on MAC 10.XX
#author - Ajay
"""
CSV file compare and produce matching case id mapping
The program will back up 
"""
import csv, os, shutil

def srchfile(directory, pattern='*'):
    if not os.path.exists(directory):
        raise ValueError("Directory not found {}".format(directory))
    dirs = []
    for root, dirnames, filenames in os.walk(directory):
        for dirname in dirnames:
                dirs.append(os.path.join(root,dirname))
                
    return dirs
#start main
old_csv = open("IN.csv","r") #master list used to create the initial structure
data = csv.reader(old_csv)
old = list(data)

#Take a backup of master file
shutil.copyfile('IN.csv', 'IN_old.csv')

new_csv = open("IN2.csv","r") #New csv from DCHub
data2 = (csv.reader(new_csv))
new = list(data2)
foundcase = {}

#close both files
old_csv.close()
new_csv.close()

for oldrow in old: 
    try:
        foundcase[oldrow[0]] = (oldrow[1])
    except (IndexError, KeyError,ValueError) as e:
        print(' Error: %s' % e) 
        
in_dir = 'root'             
in_csv2 = 'in2.csv'

sdirs = srchfile(in_dir,'*') # get dir names

for oldrow in old:
    # print foundcase
    for newrow in new: 
        if (oldrow[1] == newrow[1]):
                foundcase[newrow[0]] = foundcase.pop(oldrow[0])
                #start dir rename
                src = (os.path.join(in_dir,oldrow[0]))
                dest = (os.path.join(in_dir,newrow[0]))                
                try:
                    os.rename(src, dest)
                    print('Renaming %s to %s' %(src, dest) )
                except OSError as e:
                    print('Directory not renamed. Error: %s' % e) 
                    

# generate log file for matched case ids
newlist = open("in.csv","w")
newwriter = csv.writer(newlist)
for key, value in foundcase.items():
    data = key, value
    newwriter.writerow(data)
newlist.close()


        