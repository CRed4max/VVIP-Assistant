from FileManage.tasks.copyPaste import copyPaste


def copyPasteMethod(list):
    # list is of size 2
    # path to copy & dest path to paste

    # srcPath = input("please enter folder/file path to copy: \n")
    # destPath = input("please enter folder path to paste there: \n")

    inp = list[0]
    inp = inp.split(',')
    srcPath = inp[0]  # 1st argument srcPath
    for i in range(1, len(inp)):
        srcPath = srcPath + "\\" + inp[i]

    inp = list[1]
    inp = inp.split(',')
    destPath = inp[0]  # 2nd argument destPath
    for i in range(1, len(inp)):
        destPath = destPath + "\\" + inp[i]

    print(srcPath+" "+destPath)
    ans = copyPaste(srcPath, destPath)

    print(ans)

    return ans
