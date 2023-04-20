import glob
import networkx as nx
from numpy import number
import pandas as pd
import lib.outputValidator as ov
import lib.overheadCalc as oc
import lib.toProbe as tpb
import lib.toMininet as tmn
import lib.style as style
from lib.readTopologyZoo import GraphToMST,drawTopology

stronglyConnectedFlag = False

def toDataframe(df,topology,isBackBone,numberOfNodes,numberOfEdges,fixedNodeSender):
    #Filtering Datasets
    #if(numberOfNodes > 30):
    #    return df

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
    if(fixedNodeSender == -1):
        overheadDP_mPolkaCRC8 = oc.optimalOverhead_DataPlane_MPolkaCRC8
        overheadDP_mPolkaCRC16 = oc.optimalOverhead_DataPlane_MPolkaCRC16
        overheadDP_mPINT = oc.optimalOverhead_DataPlane_MPINT
        overheadDP_INTClassico = oc.optimalOverhead_DataPlane_INTClassico

        overheadCP_mPolkaCRC8 = oc.optimalOverhead_ControlPlane_MPolkaCRC8
        overheadCP_mPolkaCRC16 = oc.optimalOverhead_ControlPlane_MPolkaCRC16
        overheadCP_mPINT = oc.optimalOverhead_ControlPlane_MPINT
        overheadCP_INTClassico = oc.optimalOverhead_ControlPlane_INTClassico
    else:
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
            overheadDP, overheadCP = oc.extractMPINTOverhead()

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
        oc.optimalOverhead_DataPlane_INTClassico = optimalDPOverhead
        oc.optimalOverhead_ControlPlane_INTClassico = optimalCPOverhead
        tpb.sondaINTClassico = optimalProbe.copy()
    elif(approach == 'MPolka'):
        oc.optimalOverhead_DataPlane_MPolkaCRC8 = optimalDPOverhead
        oc.optimalOverhead_ControlPlane_MPolkaCRC8 = optimalCPOverhead
        tpb.dfs_init(G,optimalNodeSender)
        oc.optimalOverhead_DataPlane_MPolkaCRC16,oc.optimalOverhead_ControlPlane_MPolkaCRC16 = oc.extractMPolkaCRC16Overhead()
        tpb.sondaMPolka = optimalProbe.copy()
    elif(approach == 'MPINT'):
        oc.optimalOverhead_DataPlane_MPINT = optimalDPOverhead
        oc.optimalOverhead_ControlPlane_MPINT = optimalCPOverhead
        tpb.sondaMPINT = optimalProbe.copy()
    return optimalNodeSender

def appendGraphToDataFrame(df,G,algorithm,fixedNodeSender,topologyName,exportProbe):
    G,isBackBone,numberOfNodes,numberOfEdges = GraphToMST(G,algorithm)
    if(fixedNodeSender == -1):
        nodeSenderINTClassico = extractOptimalNodeSender(G,'INTClassico')
        tpb.dfs_init(G,nodeSenderINTClassico) #Otimizando apenas em relação ao INTClássico
        fixedNodeSender = 1
        #nodeSenderMPolka = extractOptimalNodeSender(G,'MPolka')
        #nodeSenderMPINT = extractOptimalNodeSender(G,'MPINT')

        #print(topologyName,'\n')
        #print('NS_INTClassico:',nodeSenderINTClassico,' DP:',oc.optimalOverhead_DataPlane_INTClassico)
        #print('NS_MPINT:',nodeSenderMPINT,' DP:',oc.optimalOverhead_DataPlane_MPINT)
        #print('NS_MPolka:',nodeSenderMPolka,' DP:',oc.optimalOverhead_DataPlane_MPolkaCRC8,'\n')
    else:
        tpb.dfs_init(G,fixedNodeSender)

    if(exportProbe == True):
        tpb.exportProbe(topologyName,fixedNodeSender)
    df = toDataframe(df,topologyName,isBackBone,numberOfNodes,numberOfEdges,fixedNodeSender)
    return df


def appendAllTopologysToDataFrame(df,algorithm,fixedNodeSender,draw, mininetNX):
    style.checkpoint("Filling Dataframe")
    listTopology = glob.glob(ov.toUniversalOSPath('input/*.gml'))
    for topology in listTopology:
        style.checkpoint(f"Sending Probes on {topologyName}")
        topologyName = ov.extractFilename(topology)
        G = nx.read_gml(topology,destringizer=int,label='id')
        df = appendGraphToDataFrame(df,G,algorithm,fixedNodeSender,topologyName,exportProbe=True)
        style.done()

        if(draw == True):
            style.checkpoint(f"Drawing {topologyName}")
            T = nx.minimum_spanning_tree(G,algorithm=algorithm)
            outputPath = ov.toUniversalOSPath(f'output/Topology/{topologyName}')
            drawTopology(G,T,outputPath)
            style.done()

        if(mininetNX == True):
            style.checkpoint(f"Parsing {topologyName} to MininetNX")
            ov.validateEntirePath(f'output/MininetNX')
            tmn.networkxToMininetConfig(T,topologyName,hostsPerSwitch=1)
            style.done()

    style.checkpointDone("Dataframe filled with success")
            

    return df