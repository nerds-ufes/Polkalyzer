import glob
import os
from matplotlib import pyplot as plt
import pandas as pd
import networkx as nx
import lib.outputValidator as ov

import lib.toDataframe as tdf
from lib.downloadTopologyZoo import download_series, get_links

def downloadAllTopologys():
    # Getting all links 
    links = get_links('gml') 

    # Download all links
    download_series(links)

    #Removing Bad Topologys
    print('You possibly have bad topologys in your input, we\'ll remove for you.')
    removeBadValues()

def removeBadValues():
    contTotal = 0 #Total
    cont1 = 0 #Bad Test 1
    cont2 = 0 #Bad Test 2
    cont3 = 0 #Bad Test 3
    listTopology = glob.glob('input/topologyZoo/*.gml')
    for topology in listTopology: #For Multigraph Read Error
        try:
            contTotal += 1
            G = nx.read_gml(topology,destringizer=int,label='id') #
        except:
            cont1 += 1
            print('<READ ERROR 1>',topology,'removed')
            os.remove(topology)
    listTopology = glob.glob('input/topologyZoo/*.gml')
    df = pd.DataFrame()
    for topology in listTopology: #TEST 2
        try:
            G = nx.read_gml(topology,destringizer=int,label='id')
            df = tdf.appendGraphToDataFrame(df,G=G,algorithm='prim',fixedNodeSender=-1)
        except:
            cont2 += 1
            print('<READ ERROR 2>',topology,'removed')
            os.remove(topology)
    
    df = df.loc[df['Where'] == 'DataPlane']
    df = df.loc[df['Replication Average per Node'] < 1]
    for badValue in df['Topology'].tolist(): #FOR NODES THAT GRAPHS THAT AREN'T STRONGLY CONNECTED
        cont3 += 1
        pathBadValue = 'input/topologyZoo/' + badValue + '.gml'
        print('<READ ERROR 3>',pathBadValue,'removed')
        os.remove(pathBadValue)

    print('<Topologys Removed on Test 1>: ',cont1,'/',contTotal)
    print('<Topologys Removed on Test 2>: ',cont2,'/',contTotal)
    print('<Topologys Removed on Test 2>: ',cont3,'/',contTotal)
    print('')

def drawTopology(G,T,topologyName):
    ov.validateEntirePath(f'output/Topology/{topologyName}/draw')
    nx.draw(G)
    plt.savefig(f'output/Topology/{topologyName}/draw/Graph.png',dpi=120)
    plt.clf()
    nx.draw(T)
    plt.savefig(f'output/Topology/{topologyName}/draw/MST.png',dpi=120)
    plt.clf()

def GraphToMST(G,algorithm):
    topologyName = G.graph['label'] #Hooka o atributo network que identifica o nome da Topologia
    isBackBone = G.graph['Backbone'] #Hooka o atributo backbone que identifica se a topologia é de backbone
    numberOfNodes = G.number_of_nodes()
    numberOfEdges = G.number_of_edges() #Hooka o numero de edges antes de extrair a MST
    T = nx.minimum_spanning_tree(G,algorithm=algorithm)
    drawTopology(G,T,topologyName)
    return T,topologyName,isBackBone,numberOfNodes,numberOfEdges
