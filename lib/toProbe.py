import lib.outputValidator as ov
import lib.overheadCalc as oc

sonda = []
sondaTemp = []

sondaMPolka = list()
sondaMPINT = list()
sondaINTClassico = list()

def dfs(G,v,visited,hops,previousHop): #Retorna a matriz de sondas do MPolka
    visited[v] = True
    sondaTemp.append(v)
    grau = G.degree(v)
    if(grau == 0):
        raise Exception('Graph is not strongly connected')
    
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
    oc.replicationReset()
    oc.overheadReset()
    dfs(G,v,visited,hops=0,previousHop=0)
    return sonda.copy()

def exportProbe(topologyName,fixedNodeSender):
    ov.validateEntirePath(f'output/Topology/{topologyName}')
    if(fixedNodeSender == -1):
        with open(ov.toUniversalOSPath(f'output/Topology/{topologyName}/Probe.txt'),'w') as arq:
            arq.write('MPINT: %s\n'%sondaMPINT)
            arq.write('MPolka: %s\n'%sondaMPolka)
            arq.write('INT Clássico: %s\n'%sondaINTClassico)
    else:
        with open(ov.toUniversalOSPath(f'output/Topology/{topologyName}/Probe.txt'),'w') as arq:
            arq.write('%s\n'%sonda)
