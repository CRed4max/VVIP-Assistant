import webbrowser
import os


def openFile(filePath):
    check = os.path.isfile(filePath)

    if check == False:
        # print("Invalid File Path")
        return "Invalid File Path"

    webbrowser.open_new_tab(filePath)
    # print("File Opened")
    return "File Opened"


# print("yes")
# path = "D:\Final Year Projects\FinalYear\FileManage\pajkamal.txt"
# print(os.path.isfile(path))
# openFile(path)
