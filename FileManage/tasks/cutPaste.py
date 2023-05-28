import os
import shutil
# from tasks.delete import deleteFile, deleteFolder


def cutPaste(srcPath, destPath):
    isSrcFile = os.path.isfile(srcPath)
    isSrcFolder = os.path.isdir(srcPath)
    isDestFolder = os.path.isdir(destPath)

    if isSrcFile == False and isSrcFolder == False:
        return "Invalid Path to cut Error"
    if isDestFolder == False:
        return "Invalid Destination Folder Path Error"
    

    # if os.path.exists(destPath):
    #     print('Already destination exist')

    done = shutil.move(srcPath, destPath)

    if done:
        # isFile = os.path.isfile(srcPath)
        # if isFile:
        #     deleteFile(srcPath)
        # else:
        #     deleteFolder(srcPath)

        checkCut = os.path.exists(srcPath)
        if checkCut:
            # print("patsed but didn't cut")
            return "patsed but didn't cut"
        else:
            # print("cut and pasted successfully")
            return "cut and pasted successfully"
    else:
        # print("Error while doing cut paste")
        return "Error while doing cut paste"


# working fully