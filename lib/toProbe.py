import lib.outputValidator as ov
import lib.overheadCalc as oc

sonda = []
sondaTemp = []

def dfs(G,v,visited,hops,previousHop): #Retorna a matriz de sondas do MPolka
    visited[v] = True
    sondaTemp.append(v)
    grau = G.degree(v)
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

def exportProbe(topologyName):
    ov.validateEntirePath(f'output/Topology/{topologyName}')
    with open(f'output/Topology/{topologyName}/Probe.txt','w') as arq:
        arq.write('%s\n'%sonda)