from FileManage.tasks.zip import unzip


def extractMethod(list):
    # list is of size 2
    # zip file path & destination path

    # zipFilePath = input("please enter zip file path: \n")
    # # destination folder should not exist already
    # destFolderPath = input("please enter destination folder path: \n")

    inp = list[0]
    inp = inp.split(',')
    zipFilePath = inp[0]  # 1st argument zipFilePath
    for i in range(1, len(inp)):
        zipFilePath = zipFilePath + "\\" + inp[i]

    inp = list[1]
    inp = inp.split(',')
    destFolderPath = inp[0]  # 3rd argument destFolderPath
    for i in range(1, len(inp)):
        destFolderPath = destFolderPath + "\\" + inp[i]

    unzip(zipFilePath, destFolderPath)

    print("extracted successfully")

    return "extracted successfully"
