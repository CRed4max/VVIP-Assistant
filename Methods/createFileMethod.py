from FileManage.tasks.create import createFile


def createFileMethod(list):
    # list is of size 2
    # folder path & filename with extension

    # folderPath = input("please enter folder path: \n")
    # fileName = input("please enter file name (with extension): \n")

    inp = list[0]
    inp = inp.split(',')
    folderPath = inp[0]  # 1st argument folderPath
    for i in range(1, len(inp)):
        folderPath = folderPath + "\\" + inp[i]

    fileName = list[1]   # 1st argument fileName

    ans = createFile(folderPath, fileName)

    print(ans)

    return ans

# working
