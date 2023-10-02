import glob
import lib.outputValidator as ov
from lib.readTopologyZoo import removeBadValues
import lib.toDataframe as tdf
import pandas as pd
import lib.toMininet as tmn
from pathlib import Path

def extractAnswerYN(question):
    while(True):
        print(question)
        answer = input()
        if(answer == "y" or answer == "Y"):
            return 0
        elif(answer == "n" or answer == "N"):
            return 1
        else:
            print('We doesn\'t understand your answer, answer it with (y - for yes/ n - for no)')
            print()

def mainMenu():
    print('==== Polkalyzer Main Menu ====')
    if(ov.isDir('input') == 0):
        print('Fill the ./input/ with topologys in .GML to run Polkalyzer...')
    elif(ov.isDir('input') == 1):
        removeBadValues()

    if(ov.isDir('output/MininetNX')):
        while(True):
            print('1- Run Polkalyzer')
            print('2- Modify topologys on MininetNX')
            print('My choice is: ')
            choice = int(input())
            if(choice == 1 or choice == 2):
                break
        return choice

    return 1


def topologyChoice():
    print('==== Control Plane ====')
    i=0
    listTopology = glob.glob(ov.UniversalPath('input/*.gml'))
    listTopology.sort()
    for topology in listTopology:
        topologyName = ov.extractFilename(topology)
        i+=1
        print(i,"-",topologyName)
    print('==== Control Plane ====')
    print('Choose a topology')
    print("My Choice is: ")
    choice=int(input()) -1
    topologyCustomizer(ov.extractFilename(listTopology[choice]))

def topologyCustomizer(topologyName): 
    tmn.createCustomTopology(topologyName)
    pathToImage = Path(f'output/Topology/{topologyName}/draw/TopologyNX.png')
    tmn.openImage(pathToImage)
    while(True):
        tmn.displayCustomizedComponents(topologyName)
        print(f'==== CUSTOMIZING: {topologyName} ====')
        try:
            print('What component do you wanna change?: ')
            print('1- Switch')
            print('2- Link')
            print("My Choice is: ")
            choice=int(input())
            if(choice == 1):
                print('Type the number of switch: ')
                componentNumber = int(input())
                tmn.customizeComponent(topologyName,linePrefix='s',componentNumber=componentNumber)
            elif(choice == 2):
                print('Type the number of the link: ')
                componentNumber = int(input())
                tmn.customizeComponent(topologyName,linePrefix='lss',componentNumber=componentNumber)
            else:
                print('')

            if(extractAnswerYN('Keep Customizing? (y/n):')):
                break
        except ValueError:
            print('Erro de Entrada\n')

    return choice

def algorithmChoice():
    df = pd.DataFrame() #Empty Dataframe
    print('==== Algorithm Choice ====')
    print('Answer what option do you want for algorithm')
    print('1- Default options, Polkalyzer will choice the MST and the optimal node sender for any topology')
    print('2- You\'ll choose the MST algorithm, however Polkalyzer will choose the optimal node sender for any topology')
    print('3- You\'ll choose the MST algorithm and a fixed node sender for any topologys given.')
    #DEFAULT
    algorithm = 'prim'
    fixedNodeSender = -1
    while(True):
        print('My choice is: ')
        choice = int(input())

        if(choice == 1): #Default
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender,draw=True,mininetNX=True)
            ov.validateEntirePath('output/Data/')
            df.to_csv(Path('output/Data/OptimalOverhead.csv'),index=False)
            break
        elif(choice == 2): #MST Choice
            algorithm = mstChoice()
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender,draw=True,mininetNX=True)
            ov.validateEntirePath('output/Data/')
            df.to_csv(Path(f'output/Data/Overhead_{algorithm}-Optimal.csv'),index=False)
            break
        elif(choice == 3): #MST and NodeSender Choice
            algorithm = mstChoice()
            fixedNodeSender = nodeSenderChoice()
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender,draw=True,mininetNX=True)
            ov.validateEntirePath('output/Data/')
            df.to_csv(Path(f'output/Data/Overhead_{algorithm}-{fixedNodeSender}.csv'),index=False)
            break
        else:
            print('')
    return df,choice,algorithm,fixedNodeSender

def mstChoice():
    while(True):
        print('What MST Algorithm you want choose (kruskal, prim): ')
        algorithm = input()
        if(algorithm != 'kruskal' and algorithm != 'prim'):
            print('We haven\'t this algorithm in our lib')
        else:
            return algorithm

def nodeSenderChoice():
    while(True):
        print('Type node sender id for all topologys: ')
        fixedNodeSender = int(input())
        if(ov.validateNodeSender(fixedNodeSender) == 0):
            return fixedNodeSender
        else:
            print('Your node sender can\'t be the same for all topologys\n')
