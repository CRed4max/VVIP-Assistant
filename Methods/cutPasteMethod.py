from FileManage.tasks.cutPaste import cutPaste


def cutPasteMethod(list):
    # list is of size 2
    # path to cut & dest path to paste

    srcPath = input("please enter folder/file path to cut: \n")
    destPath = input("please enter destination folder path to paste there: \n")

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
    ans = cutPaste(srcPath, destPath)

    print(ans)

    return ans
