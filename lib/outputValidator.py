import os
import lib.toDataframe as tdf
import pandas as pd
import shutil
import pathlib

# Copy folder with shutil
def copyFolder(srcPath, dstPath):
    # If path not exists, create it like with mkdir -p
    if(not(os.path.isdir(dstPath))):
        os.makedirs(dstPath)
    shutil.copytree(pathlib.Path(srcPath),pathlib.Path(dstPath))

def copyFiles(fileList, dstPath):
    # If path not exists, create it like with mkdir -p
    if(not(os.path.isdir(dstPath))):
        os.makedirs(dstPath)
    for file in fileList:
        shutil.copy(pathlib.Path(file),pathlib.Path(dstPath))

def copyFile(file, dstPath):
    # If path not exists, create it like with mkdir -p
    if(not(os.path.isdir(dstPath))):
        os.makedirs(dstPath)
    shutil.copy(pathlib.Path(file),pathlib.Path(dstPath))

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

def ensureExist(path):
    pathlib.Path(path).mkdir(parents=True, exist_ok=True)

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

def Path(rawPath):
    auxPath = rawPath.split('/')
    universalPath = ''
    for path in auxPath:
        universalPath = os.path.join(universalPath,path)
    return universalPath

def normalizePath(root,new_path):
    script_directory = os.path.dirname(os.path.abspath(__file__))
    last_occurrence_index = script_directory.rfind(root)

    if last_occurrence_index != -1:
        new_path = script_directory[:last_occurrence_index] + new_path
        return new_path
    else:
        return None
