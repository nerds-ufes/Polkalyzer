import glob
import os
import pandas as pd
import networkx as nx

import lib.toDataframe as tdf
from lib.downloadTopologyZoo import download_series, get_links

def downloadAllTopologys():
    # Getting all links 
    links = get_links('gml') 

    # Download all links
    download_series(links)

def removeBadValues():
    listTopology = glob.glob('topologyZoo/*.gml')
    for topology in listTopology:
        try:
            G = nx.read_gml(topology,destringizer=int,label='id') #
        except:
            print('<READ ERROR 1>',topology,'removed')
            os.remove(topology)
    print('PASSED TEST 1')
    for topology in listTopology:
        try:
            G = nx.read_gml(topology,destringizer=int,label='id')
            tdf.appendGraphToDataFrame(df=pd.DataFrame(),G=G)
        except:
            print('<READ ERROR 2>',topology,'removed')
            os.remove(topology)
    print('PASSED TEST 2')

def GraphToMST(G):
    topologyName = G.graph['Network'] #Hooka o atributo network que identifica o nome da Topologia
    isBackBone = G.graph['Backbone'] #Hooka o atributo backbone que identifica se a topologia é de backbone
    numberOfNodes = G.number_of_nodes()
    numberOfEdges = G.number_of_edges()
    edgeList = list(map(list,G.edges()))
    G = nx.from_edgelist(edgeList)
    T = nx.minimum_spanning_tree(G,algorithm='prim')
    edgeList = list(map(list, T.edges()))
    T = nx.from_edgelist(edgeList)

    #print(isBackBone, numberOfNodes, numberOfEdges)
    #print(edgeList)
    #print(T)
    return T,topologyName,isBackBone,numberOfNodes,numberOfEdges
