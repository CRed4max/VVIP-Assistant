from FileManage.tasks.openFile import openFile


def openFileMethod(list):
    print(list)
    path = ""
    # print("please enter path to open: \n")

    inp = list[0]
    inp = inp.split(',')
    path = inp[0]
    for i in range(1, len(inp)):
        path = path + "\\" + inp[i]

    print("this is openfilemethod")
    
    print(path)
    ans = openFile(path)

    print(ans)

# working