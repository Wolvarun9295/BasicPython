# Imported OS module.
import os

# Taking user input.
listAll = input('Enter the absolute path of directory to list all files: ')
# Listing all the files in directory.
printList = os.listdir(listAll)
for i in printList:
    print(i)
