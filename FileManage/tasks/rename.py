import os

# Renaming a file


def rename(filePath, fileOldName, fileNewName):
    check = os.path.isfile(filePath)

    if check == False:
        # print("Invalid File Path")
        return "Invalid File Path"

    startInd = filePath.rfind(fileOldName)
    print(startInd)
    endInd = filePath.rfind('.')
    new_path = filePath[0:startInd] + \
        fileNewName + filePath[endInd:len(filePath)]

    # Renaming the file
    os.rename(filePath, new_path)

    # print("Succeed")
    return "Rename Succeed"
