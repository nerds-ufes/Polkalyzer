import glob
import os
from matplotlib import pyplot as plt
import pandas as pd
import networkx as nx
import lib.outputValidator as ov

import lib.toDataframe as tdf
import lib.toProbe as tpb

from pathlib import Path

from lib.cache import is_file_cached

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

    print('\n\n === Filtered Topologys ===')
    print('<Topologys Removed on Test 1>: ',cont1,'/',contTotal)
    print('<Topologys Removed on Test 2>: ',cont2,'/',contTotal)
    print('<Topologys Removed on Test 3>: ',cont3,'/',contTotal)
    #print('<Topologys Filtered Star Based>: ',filtereds,'/',contTotal)
    print('')

def drawTopology(G,T,path):
    topologyName = path.split('/')[-1]
    plotPath = Path(f'{path}/draw/Graph.png')
    if not is_file_cached(['topology', topologyName, 'Graph'], plotPath):
        ov.validateEntirePath(ov.toUniversalOSPath(f'{path}/draw'))
        pos = nx.kamada_kawai_layout(G)
        nx.draw(
            G, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='pink', alpha=0.9,
            labels={node: node for node in G.nodes()}
        )
        plt.savefig(plotPath,dpi=120)
        plt.clf()
        plt.close()

    plotPath = Path(f'{path}/draw/MST.png')
    if not is_file_cached(['topology', topologyName, 'MST'], plotPath):
        pos = nx.kamada_kawai_layout(T)
        nx.draw(
            T, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color='red', alpha=0.9,
            labels={node: node for node in T.nodes()}
        )
        plt.savefig(ov.toUniversalOSPath(f'{path}/draw/MST.png'),dpi=120)
        plt.clf()
        plt.close()

    plotPath = Path(f'{path}/draw/TopologyNX.png')
    if not is_file_cached(['topology', topologyName, 'TNX'], plotPath):
        TNX = T
        # pos = nx.spring_layout(TNX)
        pos = nx.kamada_kawai_layout(TNX)
        for node in TNX.nodes():
            if node in tpb.sinkSwitches:
                TNX.nodes[node]['color'] = 'red'
            elif node == tpb.sonda[0][0]:
                TNX.nodes[node]['color'] = 'blue'
            else:
                TNX.nodes[node]['color'] = 'grey'
        # Draw with nx.draw with different colors
        nx.draw(
            TNX, pos, edge_color='black', width=1, linewidths=1,
            node_size=500, node_color=list(nx.get_node_attributes(TNX, 'color').values()), alpha=0.9,
            labels={node: node for node in TNX.nodes()}
        )
        nx.draw_networkx_edge_labels(
            TNX, pos,
            edge_labels = {(u, v): str(i) for i, (u, v) in enumerate(TNX.edges())},
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
