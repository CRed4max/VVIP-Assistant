import os
import shutil


def copyPaste(srcPath, destPath):
    check = os.path.isfile(srcPath)

    isSrcFile = os.path.isfile(srcPath)
    isSrcFolder = os.path.isdir(srcPath)
    print("destpath", destPath)
    isDestFolder = os.path.isdir(destPath)

    if isSrcFile == False and isSrcFolder == False:
        return "Invalid File/Folder Path to copy Error"
    if isDestFolder == False:
        return "Invalid Destination Folder Path Error"

    # print(check)
    destination = None
    if check:
        destination = shutil.copy2(srcPath, destPath)
    else:
        # print("direcotry")
        folderName = os.path.splitext(os.path.basename(srcPath))[0]
        newDestPath = os.path.join(destPath, folderName)

        destination = shutil.copytree(srcPath, newDestPath)

    # if os.path.exists(destPath):
    #     print('Already destination exist')

    if destination != None:
        # print("Successfully copied and pasted")
        return "Successfully copied and pasted"
    else:
        # print("Error while doing copy paste")
        return "Error while doing copy paste"



# working fully