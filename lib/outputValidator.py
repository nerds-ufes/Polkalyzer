import os

def validatePath(path):
    if(not(os.path.isdir(path))):
        os.mkdir(path)

def validateEntirePath(path):
    pathNames = path.split('/')
    subPath = ''
    for p in pathNames:
        subPath += p + '/' #For each subpath, verify and create
        validatePath(subPath)