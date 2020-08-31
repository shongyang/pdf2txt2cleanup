# https://pypi.org/project/pdfminer/
# https://stackoverflow.com/questions/16494447/convert-all-pdf-files-into-text-in-a-directory

import subprocess

import os
path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace(' ', 'GGG')))

path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace('&', 'HHH')))

from os import path
from glob import glob  
def find_ext(dr, ext):
    return glob(path.join(dr,"*.{}".format(ext)))

files = find_ext(".","pdf")
files = [f.replace('.\\', '') for f in files]
print(files)

checkcheck = input("TYPE 'y' BITCH: ")

if checkcheck == "y":
    for f in files:
    
        cmd = 'pdf2txt.py -o %s.txt %s' % (f.split('.')[0], f)
        run = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = run.communicate()

    # display errors if they occur    
    if err:
        print (err)
else:
    print("zzzzz")

# python pdf2txt.py -o myOutput.txt simple1.pdf
# pdf2txt.py samples/simple1.pdf

newfiles = find_ext(".","txt")
newfiles = [nf.replace('.\\', '') for nf in newfiles]
print(newfiles)

checkcheck2 = input("YOU SIGNED UP FOR NEWLINE REMOVAL THERAPY: TYPE 'y' AGAIN... BITCH: ")

if checkcheck2 == "y":

    for nf in newfiles: 
        with open(nf, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # lines = [line.strip() for line in lines]
            lines = [line.replace("\n", "") for line in lines]
        with open(nf, "w", encoding="utf-8") as f:
            f.writelines(lines) 
            # n.rstrip('\n')
            # string_without_line_breaks = " "
            # stripped_line = n.rstrip()
            # string_without_line_breaks += stripped_line
else:
    print("zzzzz")

# print(nf)
# print(nfjr)

path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace('GGG', ' ')))

path  = os.getcwd()
filenames = os.listdir(path)
for filename in filenames:
    os.rename(os.path.join(path, filename), os.path.join(path, filename.replace('HHH', '&')))