# This program creates new folders based on input given.
import os
import shutil
shutil.copy2('/src/dir/file.ext', '/dst/dir/newname.ext') # complete target filename given
shutil.copy2('/src/file.ext', '/dst/dir') # target filename is /dst/dir/file.ext

copy2(src,dst)

print('Enter Target Path:')
#TP= address1 = NEWIN('C:\\Python36\\')
TargetPath = input()
if os.getcwd() == TargetPath:
    pass
else:
    os.chdir(TargetPath)

print('Input New Folder Name?') #ask for project name
newFolder = input()
newpath = newFolder
if not os.path.exists(newpath):
       os.makedirs(newpath)
       
print('New Folder Name Saved As: ' + newFolder)

#Creating 

#Ask for Additional Project Information (CSV)
#Access Target Folder
#Save files as items in the vector
#print file name as file txt does... lame just use a connection here to the file bat... except I need to copy it to the target folder

##Exercise:
#1.Call open() to return a File Object:
#Input Source Folder:

print('Enter Source Path:')
#copied from above
SourcePath = input()
if os.getcwd() == SourcePath:
    pass
else:
    os.chdir(SourcePath)


    
filelist = open(SourcePath,  

#To do this we must pass a string path indicating the file you want to open

#2.Call read() or write() on the File object:
#3.Clse()



newAction = input()
