import os


def createFile(folderPath, fileName):
    filePath = os.path.join(folderPath, fileName)

    if os.path.exists(filePath):
        # print('file already exists')
        return "file already exists"

    with open(filePath, 'w') as fp:
        fp.write("This is new file with name " + fileName)

    check = os.path.isfile(filePath)

    if check:
        # print("File Created Successfully")
        return "File Created Successfully"
    else:
        # print("Error in creating file")
        return "Error in creating file"


def createFolder(parentFolderPath, folderName):
    folderPath = os.path.join(parentFolderPath, folderName)
    os.mkdir(folderPath)

    check = os.path.isdir(folderPath)

    if check:
        # print("Folder " + folderName+" Created Successfully")
        return "Folder " + folderName+" Created Successfully"
    else:
        # print("Error in creating folder")
        return "Error in creating folder"
