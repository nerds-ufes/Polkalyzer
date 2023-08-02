import lib.outputValidator as ov
import lib.overheadCalc as oc
from lib.polka import modified_calculate_routeid, poly_to_hex, polyList_to_hexList
from lib.cache import get_nodesID_CRC16

sonda = []
sondaTemp = []
tState = []

sondaMPolka = list()
sondaMPINT = list()
sondaINTClassico = list()

sinkSwitches = set()
nodesID_CRC16=get_nodesID_CRC16()

def getNodeID(n):
    nodesID = list()
    for i in range(n):
        nodesID.append(nodesID_CRC16[i])
    return nodesID

def dfs(G,v,visited,hops,previousHop): #Retorna a matriz de sondas do MPolka
    visited[v] = True
    sondaTemp.append(v)
    grau = G.degree(v)
    if(grau == 0):
        raise Exception('Graph is not strongly connected')

    if(grau==1):
        tState.append([1]) #Egress
    elif(hops==0):
        tState.append([1]*(grau) + [0]) #Ingress
    else:
        tState.append([1]*(grau -1) + [0]) #Core Switches

    if(grau == 1 and hops != 0):
        sinkSwitches.add(v)
    
    numberOfNodes = G.number_of_nodes()
    oc.calculaReplicationInDFS(grau)
    oc.calculaOverheads(sondaTemp,hops,numberOfNodes)
    hops += 1
    for w in G.neighbors(v):
        if grau == 1: #DEADEND
            oc.deadEndRelease(sondaTemp,hops,numberOfNodes)
        if not visited[w]:
            if grau == 2: #TRANSMISSÃO
                dfs(G,w,visited,hops,previousHop)
            else: #BIFURCAÇÃO
                previousHop = hops
                dfs(G,w,visited,hops,previousHop)

def dfs_init(G,v):
    visited=[False] * (G.number_of_nodes() + 100)
    sonda.clear()
    sondaTemp.clear()
    tState.clear()
    sinkSwitches.clear()
    oc.replicationReset()
    oc.overheadReset()
    dfs(G,v,visited,hops=0,previousHop=0)
    return sonda.copy()

def exportTopology(G,topologyName,generateNodeID,generateRouteID):
    ov.validateEntirePath(f'output/Topology/{topologyName}')
    poly_nodeIDs = getNodeID(G.number_of_nodes())
    poly_routeID = modified_calculate_routeid(poly_nodeIDs,tState,debug=False)
    routeID = poly_to_hex(poly_routeID)
    nodeIDs = polyList_to_hexList(poly_nodeIDs)
    with open(ov.toUniversalOSPath(f'output/Topology/{topologyName}/topology.toml'),'w') as arq:
        arq.write('# Usefull informations about topology\n\n')
        arq.write(f'name = "{topologyName}"\n')
        arq.write(f'numbes_of_nodes = {G.number_of_nodes()}\n')
        arq.write(f'numbes_of_edges = {G.number_of_edges()}\n')
        # arq.write(f'\n[probe]\n')
        # arq.write(f'MPINT = {sondaMPINT}\n')
        # arq.write(f'INT_Classico = {sondaINTClassico}\n')
        arq.write(f'\n[mpolka]\n')
        arq.write(f'probe = {sonda}\n')
        arq.write(f'tState = {tState}\n')
        edgeSwitches = list(sinkSwitches.copy())
        edgeSwitches.insert(0,sonda[0][0])
        arq.write(f'edgeSwitches = {edgeSwitches}\n')
        arq.write(f'number_of_edgeSwitches = {len(edgeSwitches)}\n')
        arq.write(f'number_of_coreSwitches = {G.number_of_nodes()}\n')
        if(generateNodeID):
            arq.write(f'nodesID = {nodeIDs}\n') #MinDegree = 5 for tests
        if(generateNodeID and generateRouteID):
            arq.write(f'routeID = {routeID}\n')
