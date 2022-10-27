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
    filtereds = 0 #Filtered
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
    df1 = df.loc[df['Replication Average per Node'] < 1]
    for badValue in df1['Topology'].tolist(): #FOR NODES THAT GRAPHS THAT AREN'T STRONGLY CONNECTED
        cont3 += 1
        pathBadValue = 'input/topologyZoo/' + badValue + '.gml'
        print('<READ ERROR 3>',pathBadValue,'removed')
        os.remove(pathBadValue)
    df2 = df.loc[df['Star Probability'] < 0.4] #Filtering Topologys Star Based
    df2 = df2.sort_values(by=['Star Probability','Max Replication'],ascending=[False,False])
    for goodTopology in df2['Topology'].tolist(): #FOR NODES THAT GRAPHS THAT AREN'T STRONGLY CONNECTED
        filtereds += 1
        input_pathGoodValue = 'input/topologyZoo/' + goodTopology + '.gml'
        output_pathGoodValue = 'output/Filtered Topologys/' + goodTopology + '/'
        ov.validateEntirePath(output_pathGoodValue)
        G = nx.read_gml(input_pathGoodValue,destringizer=int,label='id')
        T = nx.minimum_spanning_tree(G,algorithm='prim')
        drawTopology(G,T,output_pathGoodValue)
        print(goodTopology,'filtered to',output_pathGoodValue)

    df2.to_csv('output/Filtered Topologys/OptimalOverhead.csv')

    print('<Topologys Removed on Test 1>: ',cont1,'/',contTotal)
    print('<Topologys Removed on Test 2>: ',cont2,'/',contTotal)
    print('<Topologys Removed on Test 3>: ',cont3,'/',contTotal)
    print('<Topologys Filtered Star Based>: ',filtereds,'/',contTotal)
    print('')

def drawTopology(G,T,path):
    ov.validateEntirePath(f'{path}/draw')
    pos = nx.spring_layout(G)
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()}
    )
    plt.savefig(f'{path}/draw/Graph.png',dpi=120)
    plt.clf()
    plt.close()
    nx.draw(
        T, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='red', alpha=0.9,
        labels={node: node for node in T.nodes()}
    )
    plt.savefig(f'{path}/draw/MST.png',dpi=120)
    plt.clf()
    plt.close()

def GraphToMST(G,algorithm):
    topologyName = G.graph['label'] #Hooka o atributo network que identifica o nome da Topologia
    isBackBone = G.graph['Backbone'] #Hooka o atributo backbone que identifica se a topologia é de backbone
    numberOfNodes = G.number_of_nodes()
    numberOfEdges = G.number_of_edges() #Hooka o numero de edges antes de extrair a MST
    T = nx.minimum_spanning_tree(G,algorithm=algorithm)
    #drawTopology(G,T,f'output/Topology/{topologyName}')
    return T,topologyName,isBackBone,numberOfNodes,numberOfEdges
