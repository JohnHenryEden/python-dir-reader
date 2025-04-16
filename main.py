import os

# Count main folder
root = "./test"
fileList = os.listdir(root)
print(f"Files and directories in the main folder: {len(fileList)}")

# Prints name of empty subfolders
for dirFile in fileList:
    dirpath = root + "/" + dirFile
    # Check if it's a directory
    if(os.path.isdir(dirpath)):
        if(len(os.listdir(dirpath)) == 0):
            print(f"Empty directory name: {dirFile}")
        else:
            print(f'Non-Empty directory name: {dirFile}')
            print(f'Non-Empty directory file count: {len(os.listdir(dirpath))}')