import os
from FileManage.tasks.delete import deleteFile, deleteFolder


def deleteMethod(list):
    # list is of size 1
    # path to delete

    # path = input("please enter path to delete: \n")
    inp = list[0]
    inp = inp.split(',')
    pathToDelete = inp[0]  # 1st argument pathToDelete
    for i in range(1, len(inp)):
        pathToDelete = pathToDelete + "\\" + inp[i]
    
    print(pathToDelete)
    check = os.path.isfile(pathToDelete)

    ans = ""

    if check:
        ans = deleteFile(pathToDelete)
    else:
        ans = deleteFolder(pathToDelete)

    print(ans)

    return ans


# working