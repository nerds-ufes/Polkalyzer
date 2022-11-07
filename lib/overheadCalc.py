import lib.toProbe as tpb

replication = []

overhead_DataPlane_MPINT = []
overhead_ControlPlane_MPINT = []
overhead_DataPlane_MPolkaCRC8 = []
overhead_ControlPlane_MPolkaCRC8 = []
overhead_DataPlane_MPolkaCRC16 = []
overhead_ControlPlane_MPolkaCRC16 = []
overhead_DataPlane_INTClassico = []
overhead_ControlPlane_INTClassico = []

############## CAN BE OPTMIZED ##################
optimalOverhead_DataPlane_MPINT = []
optimalOverhead_ControlPlane_MPINT = []
optimalOverhead_DataPlane_MPolkaCRC8 = []
optimalOverhead_ControlPlane_MPolkaCRC8 = []
optimalOverhead_DataPlane_MPolkaCRC16 = []
optimalOverhead_ControlPlane_MPolkaCRC16 = []
optimalOverhead_DataPlane_INTClassico = []
optimalOverhead_ControlPlane_INTClassico = []

overhead_MPINT_Temp = []
overhead_MPolkaCRC8_Temp = []
overhead_MPolkaCRC16_Temp = []
overhead_INTClassico_Temp = []

def replicationReset():
    replication.clear()

def calculaReplicationInDFS(grau):
    if(grau == 1):
        replicationAux = 1
    else:
        replicationAux = grau - 1
    replication.append(replicationAux)

def fixReplicationVector(G,v):
    replication.pop(0) #Pop the wrong replication value (Sender Node)
    replication.append(G.degree(v)) #Append the right value (Sender Node)

def calculaOverheads(sonda,hops,numberOfNodes): #Calcula para o DataPlane
    tamanhoSonda = len(sonda)
    if(hops == 0):
        return 0 #SEM SALTOS, SEM OVERHEAD
    
    #PARA O MPINT
    overhead_MPINT_Temp.append(calculaOverheadMPINT(tamanhoSonda,hops,isCP=0))

    #PARA O MPOLKA CRC8 e CRC16
    overheadCRC8, overheadCRC16 = calculaOverheadMPolka(tamanhoSonda,isCP=0,numberOfNodes=numberOfNodes)
    overhead_MPolkaCRC8_Temp.append(overheadCRC8)
    overhead_MPolkaCRC16_Temp.append(overheadCRC16)

    #PARA O INT CLASSICO
    overhead_INTClassico_Temp.append(calculaOverheadINTClassico(hops,isCP=0))

def calculaOverheadMPINT(tamanhoSonda,hops,isCP):
    #CABEÇALHO DO MPINT
    Ethernet = 14
    Ip = 20
    INTHeader = 12
    StackINT = 48
    PathHeader = 1
    StackPath = 4
    fixo = Ethernet + Ip + INTHeader + PathHeader

    if(hops == 0):
        return 0 #SEM SALTOS, SEM OVERHEAD

    #Overhead para o MPINT
    routeOverhead = StackPath * hops
    telemetryOverhead = StackINT * (tamanhoSonda-1)
    overhead = fixo + routeOverhead + telemetryOverhead

    if(isCP == 1):
        overhead = overhead - fixo

    return overhead

def calculaOverheadMPolka(tamanhoSonda,isCP,numberOfNodes):
    #CABEÇALHO DO MPOLKA
    Ethernet = 14
    Ip = 20
    INTHeader = 12
    StackINT = 48
    routeID_CRC8 = (numberOfNodes*8)/8 #Antigo 7
    routeID_CRC16 = (numberOfNodes*16)/8 #Antigo 14
    fixo_CRC8 = Ethernet + routeID_CRC8 + Ip + INTHeader
    fixo_CRC16 = Ethernet + routeID_CRC16 + Ip + INTHeader

    #Overhead para o MPolka
    telemetryOverhead = StackINT * (tamanhoSonda-1)
    overheadCRC8 = fixo_CRC8 + telemetryOverhead
    overheadCRC16 = fixo_CRC16 + telemetryOverhead

    if(isCP == 1):
        overheadCRC8 = overheadCRC8 - Ethernet - Ip - INTHeader
        overheadCRC16 = overheadCRC16 - Ethernet - Ip - INTHeader

    return overheadCRC8,overheadCRC16

def calculaOverheadINTClassico(hops,isCP):
    #CABEÇALHO DO INT CLASSICO
    Ethernet = 14
    Ip = 20
    INTHeader = 12
    StackINT = 48
    PathHeader = 1
    StackPath = 4
    fixo = Ethernet + Ip + INTHeader + PathHeader

    if(hops == 0):
        return 0 #SEM SALTOS, SEM OVERHEAD

    #Overhead para o Int Clássico
    telemetryOverhead = StackINT + StackPath
    overhead = fixo + (telemetryOverhead * hops)

    if(isCP == 1):
        overhead = overhead - fixo

    return overhead

def overheadReset():
    overhead_DataPlane_MPINT.clear()
    overhead_ControlPlane_MPINT.clear()
    overhead_DataPlane_MPolkaCRC8.clear()
    overhead_ControlPlane_MPolkaCRC8.clear()
    overhead_DataPlane_MPolkaCRC16.clear()
    overhead_ControlPlane_MPolkaCRC16.clear()
    overhead_DataPlane_INTClassico.clear()
    overhead_ControlPlane_INTClassico.clear()

    overhead_MPolkaCRC8_Temp.clear()
    overhead_MPolkaCRC16_Temp.clear()
    overhead_MPINT_Temp.clear()
    overhead_INTClassico_Temp.clear()

def sendNewProbe(hops):
    if(len(overhead_INTClassico_Temp) == 1): #Caso ocorra replicação, ele envia uma nova sonda
        for i in range(1,hops-1): #O unico método de alcançar o próximo nó é enviando uma nova sonda.
            overhead_INTClassico_Temp.append(calculaOverheadINTClassico(i,isCP=0))
        overhead_INTClassico_Temp.append(overhead_INTClassico_Temp.pop(0)) #Joga o primeiro elemento da lista pro final

def deadEndRelease(sondaTemp,hops,numberOfNodes): #Da o append e calcula pro ControlPlane
    #RELEASE OVERHEAD MPINT
    overhead_DataPlane_MPINT.append(overhead_MPINT_Temp.copy())
    overhead_ControlPlane_MPINT.append(calculaOverheadMPINT(len(sondaTemp)+1,hops,isCP=1))
    overhead_MPINT_Temp.clear()

    #RELEASE OVERHEAD MPOLKA
    overhead_DataPlane_MPolkaCRC8.append(overhead_MPolkaCRC8_Temp.copy())
    overhead_DataPlane_MPolkaCRC16.append(overhead_MPolkaCRC16_Temp.copy())
    overheadCRC8, overheadCRC16 = calculaOverheadMPolka(len(sondaTemp)+1,isCP=1,numberOfNodes=numberOfNodes)
    overhead_ControlPlane_MPolkaCRC8.append(overheadCRC8)
    overhead_ControlPlane_MPolkaCRC16.append(overheadCRC16)
    overhead_MPolkaCRC8_Temp.clear()
    overhead_MPolkaCRC16_Temp.clear()

    #RELEASE OVERHEAD INT CLASSICO
    sendNewProbe(hops) #Caso precise replicar, ele envia uma nova sonda.
    overhead_DataPlane_INTClassico.append(overhead_INTClassico_Temp.copy())
    overhead_ControlPlane_INTClassico.append(calculaOverheadINTClassico(hops,isCP=1))
    overhead_INTClassico_Temp.clear()
    
    #RELEASE PROBE
    tpb.sonda.append(sondaTemp.copy())
    tpb.sondaTemp.clear()

def extractOverheads():
    return overhead_DataPlane_MPINT,\
        overhead_ControlPlane_MPINT,\
        overhead_DataPlane_MPolkaCRC8,\
        overhead_ControlPlane_MPolkaCRC8,\
        overhead_DataPlane_MPolkaCRC16,\
        overhead_ControlPlane_MPolkaCRC16,\
        overhead_DataPlane_INTClassico,\
        overhead_ControlPlane_INTClassico

def extractINTClassicoOverhead():
    overheadDP = sum(sum(overhead_DataPlane_INTClassico,[]))
    overheadCP = sum(overhead_ControlPlane_INTClassico)
    return overheadDP,overheadCP

def extractMPolkaCRC8Overhead():
    overheadDP = sum(sum(overhead_DataPlane_MPolkaCRC8,[]))
    overheadCP = sum(overhead_ControlPlane_MPolkaCRC8)
    return overheadDP,overheadCP

def extractMPINTOverhead():
    overheadDP = sum(sum(overhead_DataPlane_MPINT,[]))
    overheadCP = sum(overhead_ControlPlane_MPINT)
    return overheadDP,overheadCP

def extractReplication():
    return replication