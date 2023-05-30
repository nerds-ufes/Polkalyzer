import glob
import os
from matplotlib import pyplot as plt
import pandas as pd
import networkx as nx
import lib.outputValidator as ov

import lib.toDataframe as tdf
import lib.toProbe as tpb

def removeBadValues():
    contTotal = 0 #Total
    cont1 = 0 #Bad Test 1
    cont2 = 0 #Bad Test 2
    cont3 = 0 #Bad Test 3
    filtereds = 0 #Filtered
    listTopology = glob.glob(os.path.join('input','*.gml'))
    for topology in listTopology: #For Multigraph Read Error
        try:
            contTotal += 1
            G = nx.read_gml(topology,destringizer=int,label='id') #
        except:
            cont1 += 1
            print('<READ ERROR 1>',topology,'removed')
            os.remove(topology)
    listTopology = glob.glob(os.path.join('input','*.gml'))
    df = pd.DataFrame()
    for topology in listTopology: #TEST 2
        try:
            G = nx.read_gml(topology,destringizer=int,label='id')
            topologyName = ov.extractFilename(topology)
            df = tdf.appendGraphToDataFrame(df,G=G,algorithm='prim',fixedNodeSender=-1,topologyName=topologyName,exportTopology=False)

        except:
            cont2 += 1
            print('<READ ERROR 2>',topology,'removed')
            os.remove(topology)

    df = df.loc[df['Where'] == 'DataPlane']
    df1 = df.loc[df['Replication Average per Node'] < 1]
    for badValue in df1['Topology'].tolist(): #FOR NODES THAT GRAPHS THAT AREN'T STRONGLY CONNECTED
        cont3 += 1
        pathBadValue = os.path.join('input/',badValue,'.gml')
        print('<READ ERROR 3>',pathBadValue,'removed')
        os.remove(pathBadValue)

    #FILTERING STAR PROBABILITY TOPOLOGYS
    #df1 = df.loc[df['Replication Average per Node'] >= 1] #Drop bad Values
    #df2 = df1.loc[df1['Star Probability'] < 0.4] #Filtering Topologys Star Based
    #df2 = df2.sort_values(by=['Star Probability','Max Replication'],ascending=[False,False])
    #print('Filtered Topologys Path: output/Filtered Topologys/')
    #for goodTopology in df2['Topology'].tolist(): #FOR NODES THAT GRAPHS THAT AREN'T STRONGLY CONNECTED
    #    filtereds += 1
    #    input_pathGoodValue = 'input/' + goodTopology + '.gml'
    #    output_pathGoodValue = 'output/Filtered Topologys/' + goodTopology + '/'
    #    ov.validateEntirePath(output_pathGoodValue)
    #    G = nx.read_gml(input_pathGoodValue,destringizer=int,label='id')
    #    T = nx.minimum_spanning_tree(G,algorithm='prim')
    #    drawTopology(G,T,output_pathGoodValue)
    #    print('Filtered:',goodTopology)

    #df2.to_csv('output/Filtered Topologys/OptimalOverhead.csv')

    print('<Topologys Removed on Test 1>: ',cont1,'/',contTotal)
    print('<Topologys Removed on Test 2>: ',cont2,'/',contTotal)
    print('<Topologys Removed on Test 3>: ',cont3,'/',contTotal)
    #print('<Topologys Filtered Star Based>: ',filtereds,'/',contTotal)
    print('')

def drawTopology(G,T,path):
    ov.validateEntirePath(ov.toUniversalOSPath(f'{path}/draw'))
    pos = nx.kamada_kawai_layout(G)
    nx.draw(
        G, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='pink', alpha=0.9,
        labels={node: node for node in G.nodes()}
    )
    plt.savefig(ov.toUniversalOSPath(f'{path}/draw/Graph.png'),dpi=120)
    plt.clf()
    plt.close()
    pos = nx.kamada_kawai_layout(T)
    nx.draw(
        T, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='red', alpha=0.9,
        labels={node: node for node in T.nodes()}
    )
    plt.savefig(ov.toUniversalOSPath(f'{path}/draw/MST.png'),dpi=120)
    plt.clf()
    plt.close()
    # criar um dicionário com peso fixo 10 para cada aresta
    edge_weights = {(u, v): 10 for u, v in T.edges()}
    # atribuir os pesos fixos às arestas do grafo
    nx.set_edge_attributes(T, edge_weights, 'my_weight')
    # aplicar o layout com os pesos atribuídos
    pos = nx.spring_layout(T, weight='my_weight')
    nx.draw(
        T, pos, edge_color='black', width=1, linewidths=1,
        node_size=500, node_color='red', alpha=0.9,
        labels={node: node for node in T.nodes()}
    )
    nx.draw_networkx_edge_labels(
        G, pos,
        edge_labels = {(u, v): str(i) for i, (u, v) in enumerate(T.edges())},
        font_color='red', alpha=0.7, font_size=7
    )
    plt.savefig(ov.toUniversalOSPath(f'{path}/draw/TopologyNX.png'),dpi=120)
    plt.clf()
    plt.close()

def GraphToMST(G,algorithm):
    #topologyName = G.graph['label'] #Hooka o atributo network que identifica o nome da Topologia
    isBackBone = G.graph['Backbone'] #Hooka o atributo backbone que identifica se a topologia é de backbone
    numberOfNodes = G.number_of_nodes()
    numberOfEdges = G.number_of_edges() #Hooka o numero de edges antes de extrair a MST
    T = nx.minimum_spanning_tree(G,algorithm=algorithm)
    #drawTopology(G,T,f'output/Topology/{topologyName}')
    return T,isBackBone,numberOfNodes,numberOfEdges
