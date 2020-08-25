import os

sourceCSVFile = open("/home/madhup/Documents/dev/folderInfo.csv" , "w")
sourceFolder = "/home/madhup/Documents/postgre/postgresql-12.3"
folderArr=[sourceFolder]
fileEntry = "file"
folderEntry = "folder"


"""
def defineFile(path, fileName):
    sourceCSV = open(path + "/" + fileName + ".csv" ,"w")
"""

def inputSrcInfo (folderPath):
    outerCount = 0
    entryCount = 0
    newEntry = ""
    subDirCount = 0
    folderLevel = 0
    folderAdded = False

    sourceCSVFile.write("Sl" + "\t" + "Level" + "\t" + "Type" + "\t" + "Parent Folder" + "\t" + "Curr File" + "\n")

    while outerCount < len(folderArr):
        folderList = os.listdir(folderArr[outerCount])

        parentFolder = folderArr[outerCount]
        debugStr = "Folder Array Len is {}. Folder Name in outer count is {}.\n Sub Dir Count is {}. Folder Level is {}."
        
        outerCount += 1
        newEntry = ""

        """
        if(subDirCount + folderLevel == len(folderArr) - 1 and folderAdded == True):
            folderLevel += 1
            subDirCount = 0
            folderAdded = False

        """
        folderAdded = False
        print(debugStr.format(len(folderArr), parentFolder, subDirCount, folderLevel))

        for entry in folderList:
            childEntry = parentFolder + "/" + entry
            entryCount += 1
            
            newEntry = str(entryCount) + "\t" + str(folderLevel) +"\t"
            newDebugStr = "Child in parent folder is {}. It is of the type {}.\n OuterCount is {}. Folder Level is {}.\n New Folder Array Length is {}. Entry in CSV File is {}."
            if (os.path.isdir(childEntry)):
                folderArr.append(childEntry)
                folderAdded = True
                newEntry += folderEntry + "\t" + parentFolder + "\t" + entry + "\n"
                ##print(newDebugStr.format(childEntry, folderEntry, str(outerCount), str(folderLevel), str(len(folderArr)), newEntry))
                subDirCount += 1
                
                sourceCSVFile.write(newEntry)
            else:
                newEntry += fileEntry + "\t" + parentFolder + "\t" + entry + "\n"
                ##print(newDebugStr.format(childEntry, fileEntry, str(outerCount), str(folderLevel),str(len(folderArr)), newEntry))
                sourceCSVFile.write(newEntry)


inputSrcInfo(sourceFolder)