import os
import lib.toDataframe as tdf
import pandas as pd

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
    pathNames = path.split('/')
    subPath = ''
    for p in pathNames:
        subPath += p + '/' #For each subpath, verify and create
        validatePath(subPath)

def validateNodeSender(fixedNodeSender):
    try:
        tdf.appendAllTopologysToDataFrame(pd.DataFrame(),algorithm='prim',fixedNodeSender=fixedNodeSender,draw=False)
        return 0
    except:
        return 1

def extractFilename(path):
    fileName = path.split('/')
    fileName = fileName.pop()
    fileName = fileName.split('.')
    fileName = fileName.pop(0)
    #print(fileName)
    return fileName

def extractPathFile(path):
    pathFile = path.split('/')
    pathFile.pop()
    folderPath = ''
    for subPath in pathFile:
        folderPath += subPath + '/'
    #print(folderPath)
    return folderPath

def validateEntirePathFile(path):
    newPath = extractPathFile(path)
    pathNames = newPath.split('/')
    subPath = ''
    for p in pathNames:
        subPath += p + '/' #For each subpath, verify and create
        validatePath(subPath)