import os
import shutil


# for compressing a folder into zip file
def zipdir(folderPath, createdFileName, destFolder):
    checkDestFolder = os.path.isdir(destFolder)
    checkFolderPath = os.path.isdir(folderPath)

    if checkFolderPath == False:
        return "Invalid Folder to zip Error"
    if checkDestFolder == False:
        return "Invalid Destination Folder"
    
    firstParameter = os.path.join(destFolder, createdFileName)
    shutil.make_archive(firstParameter, format='zip', root_dir=folderPath)

    outputFile = firstParameter + '.zip'
    isoutputFileFile  = os.path.isfile(outputFile)

    if isoutputFileFile:
        print("zipped file: " + outputFile)
        return "Folder Successfully zipped"
    else:
        return "Error while zipping the Folder"



def unzip(zipFilePath, destFolderPath):
    shutil.unpack_archive(zipFilePath, destFolderPath)




# folder to zip is working
# file to zip is not working
# unzip is not working