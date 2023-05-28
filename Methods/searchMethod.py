from FileManage.tasks.search import searchFile


def searchMethod(list):
    # filename with extensions
    # fileName = input("please enter file name (with extension) to search: \n")
    # searchPath = input("please enter search directory path: \n")

    print("in search function")

    fileName = list[0]  # 1st argument fileName

    inp = list[1]
    inp = inp.split(',')
    searchPath = inp[0]  # 2nd argument searchPath
    for i in range(1, len(inp)):
        searchPath = searchPath + "\\" + inp[i]


    print(searchPath)

    ans = searchFile(fileName, searchPath)

    if len(ans) == 0:
        print("No such file present")
    else:
        print("Present files are: ")
        print(ans)

    return ans

# working