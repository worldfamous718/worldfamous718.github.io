#
# World McCrea
# 7/11/2024
# Program using os and os.path
#

import os

# let me handle the first part of this code
# list the files and dirs
# I tried defining main first but had issues

def show_files_and_dirs():
    contents = os.listdir()  # store my directory items in a variable
    print('Files and directories in current directory:')
    for item in contents:
        print(item)  # print out my file list

def main():
    show_files_and_dirs()
    # check if my file is present. should be if the item is a file
    if os.path.isfile('info.txt'):

        # rename the present file
        os.rename('info.txt', 'information.txt')

    else:
        # message for if file not found
        print('File info.txt does not exist. Cannot rename.')

    if os.path.exists('information'): # check for my file?
        print('Directory information already exists. Cannot create.')
    else:
        # create the directory and let user know
        os.mkdir('information')
        print("'information' directory has been created")

    # call show files function
    show_files_and_dirs()

main()




