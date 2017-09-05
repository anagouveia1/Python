# This program creates new folders based on input given.
import os
address1 = 'C:\\Python36\\'
if os.getcwd() == address1:
    pass
else:
    os.chdir('C:\\Python\\')

print('Hello World!')
print('Input New Folder Name?') #ask for project name
newFolder = input()
newpath = newFolder
if not os.path.exists(newpath):
       os.makedirs(newpath)
print('New Folder Name Saved As: ' + newFolder)

#Ask for Additional Project Information (CSV)

