from FileManage.tasks.create import createFolder


def createFolderMethod(list):
    # list is of size 2
    # parent folder path & folderName

    # parentFolderPath = input("please enter parent folder path: \n")
    # folderName = input("please enter folder name: \n")

    inp = list[0]
    inp = inp.split(',')
    parentFolderPath = inp[0]  # 1st argument parentFolderPath
    for i in range(1, len(inp)):
        parentFolderPath = parentFolderPath + "\\" + inp[i]

    folderName = list[1]   # 1st argument folderName

    ans = createFolder(parentFolderPath, folderName)

    print(ans)

    return ans

# working
# intents not efficient with : make a directory
