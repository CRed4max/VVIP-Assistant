from FileManage.tasks.rename import rename


def renameMethod(list):
    # list is of size 2 here
    # file path & newname

    # filePath = input("enter path to rename: \n")
    # fileOldName = input("enter file's old name (without extension): \n")
    # fileNewName = input("enter file's new name (without extension): \n")

    inp = list[0]
    inp = inp.split(',')
    filePath = inp[0]  # 1st argument filePath
    for i in range(1, len(inp)):
        filePath = filePath + "\\" + inp[i]
    
    print("filePath: ", filePath)

    fileOldName = inp[len(inp) - 1].split('.')[0]   # 2nd argument fileOldName
    fileNewName = list[1]  # 3rd argument fileNewName


    ans = rename(filePath, fileOldName, fileNewName)

    print(ans)

    return ans

# Working 