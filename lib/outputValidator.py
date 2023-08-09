import os
import lib.toDataframe as tdf
import pandas as pd
import shutil
from pathlib import Path

# Copy folder with shutil
def copyFolder(srcPath, dstPath):
    shutil.copytree(Path(srcPath),Path(dstPath))

def copyFiles(fileList, dstPath):
    for file in fileList:
        shutil.copy(Path(file),Path(dstPath))

def copyFile(file, destPath):
    shutil.copy(Path(file),Path(destPath))

def isDir(path):
    if(os.path.isdir(path)):
        return 1
    else:
        return 0

def isFile(path):
    if(os.path.isfile(path)):
        return 1
    else:
        return 0

def validatePath(path):
    if(not(os.path.isdir(path))):
        os.mkdir(path)

def validateEntirePath(path):

    if(os.name == 'posix'):
        pathNames = path.split('/')
    else:
        pathNames = path.split('\\')
    
    subPath = ''
    for p in pathNames:
        subPath += p + '/' #For each subpath, verify and create
        validatePath(subPath)

def validateNodeSender(fixedNodeSender):
    try:
        tdf.appendAllTopologysToDataFrame(pd.DataFrame(),algorithm='prim',fixedNodeSender=fixedNodeSender,draw=False,mininetNX=False)
        return 0
    except:
        return 1

def extractFilename(path):
    if(os.name == 'posix'):
        fileName = path.split('/')
    else:
        fileName = path.split('\\')
    
    fileName = fileName.pop()
    fileName = fileName.split('.')
    fileName = fileName.pop(0)
    #print(fileName)
    return fileName

def extractPathFile(path):
    if(os.name == 'posix'):
        pathFile = path.split('/')
    else:
        pathFile = path.split('\\')

    pathFile.pop()
    folderPath = ''

    if(os.name == 'posix'):
        for subPath in pathFile:
            folderPath += subPath + '/'
        #print(folderPath)
    else:
        for subPath in pathFile:
            folderPath += subPath + '\\'
        #print(folderPath)
    
    return folderPath

def validateEntirePathFile(path):
    newPath = extractPathFile(path)
    if(os.name == 'posix'):
        pathNames = newPath.split('/')
    else:
        pathNames = newPath.split('\\')
    subPath = ''
    for p in pathNames:
        subPath += p + '/' #For each subpath, verify and create
        validatePath(subPath)

def toUniversalOSPath(rawPath):
    auxPath = rawPath.split('/')
    universalPath = ''
    for path in auxPath:
        universalPath = os.path.join(universalPath,path)
    return universalPath
