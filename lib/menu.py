import lib.outputValidator as ov
from lib.readTopologyZoo import downloadAllTopologys, removeBadValues
import lib.toProbe as tpb
import lib.toDataframe as tdf
import pandas as pd
import lib.plots as pplt

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
    print('==== Polka Analyzer Tool ====')
    if(ov.isDir('input/topologyZoo') == 0):
        print('You don\'t have topologys downloaded, press enter to start download ...')
        downloadAllTopologys()
    elif(ov.isDir('input/topologyZoo') == 1):
        if(extractAnswerYN('Do you want download more topologys (y/n): ') == 0):
            downloadAllTopologys()
        else:
            removeBadValues()

    df,choice,algorithm,fixedNodeSender = algorithmChoice()

    if(choice == 1):
        pplt.OverheadPointPlot(df,f'output/Plots/OverheadPP')
        pplt.OverheadLinePlot(df,f'output/Plots/OverheadLP')
        pplt.StateOverheadJointPlot(df,f'output/Plots/OverheadJP')
    elif(choice == 2):
        pplt.OverheadPointPlot(df,f'output/Plots/OverheadPP-{algorithm}-WithOtimization')
        pplt.OverheadLinePlot(df,f'output/Plots/OverheadLP-{algorithm}-WithOtimization')
        pplt.StateOverheadJointPlot(df,f'output/Plots/OverheadJP-{algorithm}-WithOtimization')
    elif(choice == 3):
        pplt.OverheadPointPlot(df,f'output/Plots/OverheadPP-{algorithm}-{fixedNodeSender}')
        pplt.OverheadLinePlot(df,f'output/Plots/OverheadLP-{algorithm}-{fixedNodeSender}')
        pplt.StateOverheadJointPlot(df,f'output/Plots/OverheadJP-{algorithm}-{fixedNodeSender}')

    return df

def algorithmChoice():
    df = pd.DataFrame(columns=['Topology','Where','IsBackBone','Number of Nodes','Number of Edges','Replication Average per Node','Max Replication','State Overhead','MPolka CRC8','MPolka CRC16','MPINT','INT Clássico']) #Empty Row Dataframe
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
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender)
            ov.validateEntirePath('output/Data/')
            df.to_csv('output/Data/OptimalOverhead.csv',index=False)
            break
        elif(choice == 2): #MST Choice
            algorithm = mstChoice()
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender)
            ov.validateEntirePath('output/Data/')
            df.to_csv(f'output/Data/Overhead_{algorithm}-Optimal.csv',index=False)
            break
        elif(choice == 3): #MST and NodeSender Choice
            algorithm = mstChoice()
            fixedNodeSender = nodeSenderChoice()
            df = tdf.appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender)
            ov.validateEntirePath('output/Data/')
            df.to_csv(f'output/Data/Overhead_{algorithm}-{fixedNodeSender}.csv',index=False)
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
