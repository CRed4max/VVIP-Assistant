from FileManage.tasks.zip import zipdir


def zipMethod(list):
    # list is of size 3
    # path to zip & name of output zip file & destination path
    
    # folderPath = input("please enter folder/file path to zip: \n")
    # createdFileName = input("please enter name of your output zip file (without extension): \n")
    # destFolder = input("please enter destination folder: \n")

    inp = list[0]
    inp = inp.split(',')
    folderPath = inp[0]  # 1st argument path to zip
    for i in range(1, len(inp)):
        folderPath = folderPath + "\\" + inp[i]

    createdFileName = list[1]  # 2nd argument createdFileName

    inp = list[2]
    inp = inp.split(',')
    destFolder = inp[0]  # 3rd argument destFolder
    for i in range(1, len(inp)):
        destFolder = destFolder + "\\" + inp[i]

    print(folderPath, createdFileName, destFolder)
    ans = zipdir(folderPath, createdFileName, destFolder)

    print(ans)

    return ans
