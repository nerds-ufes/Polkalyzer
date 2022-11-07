import glob
import networkx as nx
from numpy import number
import pandas as pd

import lib.outputValidator as ov
import lib.overheadCalc as oc
import lib.toProbe as tpb
from lib.readTopologyZoo import GraphToMST,drawTopology


def toDataframe(df,topology,isBackBone,numberOfNodes,numberOfEdges):
    #Filtering Datasets
    if(numberOfNodes > 50):
        return df

    #Extracting Overheads
    overhead_DataPlane_MPINT,\
    overhead_ControlPlane_MPINT,\
    overhead_DataPlane_MPolkaCRC8,\
    overhead_ControlPlane_MPolkaCRC8,\
    overhead_DataPlane_MPolkaCRC16,\
    overhead_ControlPlane_MPolkaCRC16,\
    overhead_DataPlane_INTClassico,\
    overhead_ControlPlane_INTClassico = oc.extractOverheads()
    replication = oc.extractReplication()
    
    #Overhead por abordagem
    overheadDP_mPolkaCRC8 = sum(sum(overhead_DataPlane_MPolkaCRC8,[]))
    overheadDP_mPolkaCRC16 = sum(sum(overhead_DataPlane_MPolkaCRC16,[]))
    overheadDP_mPINT = sum(sum(overhead_DataPlane_MPINT,[]))
    overheadDP_INTClassico = sum(sum(overhead_DataPlane_INTClassico,[]))

    overheadCP_mPolkaCRC8 = sum(overhead_ControlPlane_MPolkaCRC8)
    overheadCP_mPolkaCRC16 = sum(overhead_ControlPlane_MPolkaCRC16)
    overheadCP_mPINT = sum(overhead_ControlPlane_MPINT)
    overheadCP_INTClassico = sum(overhead_ControlPlane_INTClassico)

    replicationPerNode = sum(replication)/numberOfNodes
    maxReplication = max(replication)
    stateOverhead = 0
    for n in replication:
        stateOverhead += (1 + 2*n)

    starProbability = (maxReplication+1)/numberOfNodes

    matrixOverhead = {}
    matrixOverhead['Topology'] = [topology,topology]
    matrixOverhead['IsBackBone'] = [isBackBone,isBackBone]
    matrixOverhead['Number of Nodes'] = [numberOfNodes,numberOfNodes]
    matrixOverhead['Number of Edges'] = [numberOfEdges,numberOfEdges]
    matrixOverhead['Replication Average per Node'] = [replicationPerNode,replicationPerNode]
    matrixOverhead['Max Replication'] = [maxReplication,maxReplication]
    matrixOverhead['State Overhead'] = [stateOverhead,stateOverhead]
    matrixOverhead['Star Probability'] = [starProbability,starProbability]
    matrixOverhead['Where'] = ['DataPlane','ControlPlane']
    matrixOverhead['MPINT'] = [overheadDP_mPINT,overheadCP_mPINT]
    matrixOverhead['MPolka CRC8'] = [overheadDP_mPolkaCRC8,overheadCP_mPolkaCRC8]
    matrixOverhead['MPolka CRC16'] = [overheadDP_mPolkaCRC16,overheadCP_mPolkaCRC16]
    matrixOverhead['INT Clássico'] = [overheadDP_INTClassico,overheadCP_INTClassico]
    df2 = pd.DataFrame(data=matrixOverhead)
    result = pd.concat([df,df2],ignore_index=True)
    return result

def extractOptimalNodeSender(G,approach): #Optimal on DP as tiebreaker, Optimal on MPOLKA CRC16
    optimalDPOverhead = 10000000 #Infinite
    optimalCPOverhead = 10000000 #Infinite
    optimalNodeSender = 0
    optimalProbe = 0
    overheadDP = 0
    overheadCP = 0
    for nodeSender in G.nodes():
        sonda = tpb.dfs_init(G,nodeSender)
        if(approach == 'INTClassico'):
            overheadDP, overheadCP = oc.extractINTClassicoOverhead()
        elif(approach == 'MPolka'):
            overheadDP, overheadCP = oc.extractMPolkaCRC8Overhead()
        elif(approach == 'MPINT'):
            overheadDP, overheadCP = oc.extractMPINTOverhead

        #print('Possivel Matriz de Sondas: ',sonda,'Overhead DP:',overheadDP,'| Overhead CP',overheadCP)

        if((overheadDP < optimalDPOverhead) and (overheadCP < optimalCPOverhead)):
            optimalDPOverhead = overheadDP
            optimalCPOverhead = overheadCP
            optimalProbe = sonda
            optimalNodeSender = nodeSender
        elif((overheadDP < optimalDPOverhead) and (overheadCP == optimalCPOverhead)):
            optimalDPOverhead = overheadDP
            optimalCPOverhead = overheadCP
            optimalProbe = sonda
            optimalNodeSender = nodeSender
        elif((overheadDP == optimalDPOverhead) and (overheadCP < optimalCPOverhead)):
            optimalDPOverhead = overheadDP
            optimalCPOverhead = overheadCP
            optimalProbe = sonda
            optimalNodeSender = nodeSender
        elif((overheadDP > optimalDPOverhead) and (overheadCP < optimalCPOverhead)):
            if((overheadDP + overheadCP) < (optimalDPOverhead + optimalCPOverhead)):
                optimalDPOverhead = overheadDP
                optimalCPOverhead = overheadCP
                optimalProbe = sonda
                optimalNodeSender = nodeSender
    #print('<Escolhida> ',optimalNodeSender)
    if(approach == 'INTClassico'):
        tpb.sondaINTClassico = tpb.sonda.copy()
        oc.optimalOverhead_DataPlane_INTClassico = oc.overhead_DataPlane_INTClassico.copy()
        oc.optimalOverhead_ControlPlane_INTClassico = oc.overhead_ControlPlane_INTClassico.copy()
        tpb.sondaINTClassico = optimalProbe
    elif(approach == 'MPolka'):
        oc.optimalOverhead_DataPlane_MPolkaCRC8 = oc.overhead_DataPlane_MPolkaCRC8.copy()
        oc.optimalOverhead_ControlPlane_MPolkaCRC8 = oc.overhead_ControlPlane_MPolkaCRC8.copy()
        oc.optimalOverhead_DataPlane_MPolkaCRC16 = oc.overhead_DataPlane_MPolkaCRC16.copy()
        oc.optimalOverhead_ControlPlane_MPolkaCRC16 = oc.overhead_ControlPlane_MPolkaCRC16.copy()
        tpb.sondaMPolka = optimalProbe
    elif(approach == 'MPINT'):
        oc.optimalOverhead_DataPlane_MPINT = oc.overhead_DataPlane_MPINT.copy()
        oc.optimalOverhead_ControlPlane_MPINT = oc.overhead_ControlPlane_MPINT.copy()
        tpb.sondaMPINT = optimalProbe
    return optimalNodeSender

def appendGraphToDataFrame(df,G,algorithm,fixedNodeSender,topologyName,exportProbe):
    G,isBackBone,numberOfNodes,numberOfEdges = GraphToMST(G,algorithm)
    nodeSender = 0
    nodeSenderINTClassico = 0
    nodeSenderMPolka = 0
    nodeSenderMPINT = 0
    if(fixedNodeSender == -1):
        nodeSenderINTClassico = extractOptimalNodeSender(G,'INTClassico')
        nodeSenderMPolka = extractOptimalNodeSender(G,'MPolka')
        nodeSenderMPINT = extractOptimalNodeSender(G,'MPINT')
    else:
        nodeSender = fixedNodeSender

    tpb.dfs_init(G,nodeSender)
    if(exportProbe == True):
        tpb.exportProbe(topologyName)
    df = toDataframe(df,topologyName,isBackBone,numberOfNodes,numberOfEdges)
    return df


def appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender,draw):
    listTopology = glob.glob('input/topologyZoo/*.gml')
        
    for topology in listTopology:
        topologyName = ov.extractFilename(topology)
        G = nx.read_gml(topology,destringizer=int,label='id')
        df = appendGraphToDataFrame(df,G,algorithm,fixedNodeSender,topologyName,exportProbe=True)
        if(draw == True):
            T = nx.minimum_spanning_tree(G,algorithm=algorithm)
            outputPath = f'output/Topology/{topologyName}'
            drawTopology(G,T,outputPath)
    return df