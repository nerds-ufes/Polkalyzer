import lib.outputValidator as ov
import lib.overheadCalc as oc
from polka.tools import calculate_routeid, generate_nodeids

sonda = []
sondaTemp = []
tState = []

sondaMPolka = list()
sondaMPINT = list()
sondaINTClassico = list()

sinkSwitches = set()

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
    
    numberOfNodes = G.number_of_nodes()
    oc.calculaReplicationInDFS(grau)
    oc.calculaOverheads(sondaTemp,hops,numberOfNodes)
    hops += 1
    for w in G.neighbors(v):
        if grau == 1: #DEADEND
            sinkSwitches.add(w)
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
    nodeIDs = generate_nodeids(5,G.number_of_nodes()) #MinDegree = 5 for tests
    routeID = calculate_routeid(nodeIDs,tState,debug=False)
    with open(ov.toUniversalOSPath(f'output/Topology/{topologyName}/topology.toml'),'w') as arq:
        arq.write('# Usefull informations about topology\n\n')
        arq.write(f'name = {topologyName}\n')
        arq.write(f'numbes_of_nodes = {G.number_of_nodes()}\n')
        arq.write(f'numbes_of_edges = {G.number_of_edges()}\n')
        # arq.write(f'\n[probe]\n')
        # arq.write(f'MPINT = {sondaMPINT}\n')
        # arq.write(f'INT_Classico = {sondaINTClassico}\n')
        arq.write(f'\n[mpolka]\n')
        arq.write(f'probe = {sonda}\n')
        arq.write(f'tState = {tState}\n')
        if(generateNodeID):
            arq.write(f'nodesID = {nodeIDs}\n') #MinDegree = 5 for tests
        if(generateNodeID and generateRouteID):
            arq.write(f'routeID = {routeID}\n')
