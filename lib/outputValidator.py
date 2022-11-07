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
        tdf.appendAllTopologysToDataFrame(pd.DataFrame(),algorithm='prim',fixedNodeSender=fixedNodeSender)
        return 0
    except:
        return 1

def extractFilename(path):
    fileName = path.split('/')
    fileName = fileName.pop()
    fileName = fileName.split('.')
    fileName = fileName.pop(0)
    return fileName
    #print(fileName)