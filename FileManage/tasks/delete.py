import os
import shutil


def deleteFile(filePath):
    print("your delete function initiated")
    check = os.path.isfile(filePath)

    if check == False:
        # print("Invalid File Path here")
        return "Invalid File Path here"

    os.remove(filePath)
    # print("File deleted")
    return "File deleted"


def deleteFolder(folderPath):
    check = os.path.isdir(folderPath)

    if check == False:
        # print("Invalid Folder Path here")
        return "Invalid Folder Path here"

    shutil.rmtree(folderPath)
    # print("Folder deleted")
    return "Folder deleted"
