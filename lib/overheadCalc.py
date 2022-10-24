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

def calculaOverheads(sonda,hops):
    tamanhoSonda = len(sonda)
    if(hops == 0):
        return 0 #SEM SALTOS, SEM OVERHEAD
    
    #PARA O MPINT
    overhead_MPINT_Temp.append(calculaOverheadMPINT(tamanhoSonda,hops))

    #PARA O MPOLKA CRC8 e CRC16
    overheadCRC8, overheadCRC16 = calculaOverheadMPolka(tamanhoSonda)
    overhead_MPolkaCRC8_Temp.append(overheadCRC8)
    overhead_MPolkaCRC16_Temp.append(overheadCRC16)

    #PARA O INT CLASSICO
    overhead_INTClassico_Temp.append(calculaOverheadINTClassico(hops))

def calculaOverheadMPINT(tamanhoSonda,hops):
    #CABEÇALHO DO MPINT
    mPINT_Ethernet = 14
    mPINT_Ip = 20
    mPINT_INTHeader = 12
    mPINT_StackINT = 48
    mPINT_PathHeader = 1
    mPINT_StackPath = 4
    fixo_MPINT = mPINT_Ethernet + mPINT_Ip + mPINT_INTHeader + mPINT_PathHeader

    if(hops == 0):
        return 0 #SEM SALTOS, SEM OVERHEAD

    #Overhead para o MPINT
    routeOverheadMPINT = mPINT_StackPath * hops
    telemetryOverheadMPINT = mPINT_StackINT * (tamanhoSonda-1)
    overhead = fixo_MPINT + routeOverheadMPINT + telemetryOverheadMPINT
    return overhead

def calculaOverheadMPolka(tamanhoSonda):
    #CABEÇALHO DO MPOLKA
    mPolka_Ethernet = 14
    mPolka_Ip = 20
    mPolka_INTHeader = 12
    mPolka_StackINT = 48
    mPolka_routeID_CRC8 = 7
    mPolka_routeID_CRC16 = 14
    fixo_MPolkaCRC8 = mPolka_Ethernet + mPolka_routeID_CRC8 + mPolka_Ip + mPolka_INTHeader
    fixo_MPolkaCRC16 = mPolka_Ethernet + mPolka_routeID_CRC16 + mPolka_Ip + mPolka_INTHeader

    #Overhead para o MPolka
    telemetryOverheadMPolka = mPolka_StackINT * (tamanhoSonda-1)
    overheadCRC8 = fixo_MPolkaCRC8 + telemetryOverheadMPolka
    overheadCRC16 = fixo_MPolkaCRC16 + telemetryOverheadMPolka

    return overheadCRC8,overheadCRC16

def calculaOverheadINTClassico(hops):
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

def sendNewProbe(hops):
    if(len(overhead_INTClassico_Temp) == 1): #Caso ocorra replicação, ele envia uma nova sonda
        for i in range(1,hops-1): #O unico método de alcançar o próximo nó é enviando uma nova sonda.
            overhead_INTClassico_Temp.append(calculaOverheadINTClassico(i))
        overhead_INTClassico_Temp.append(overhead_INTClassico_Temp.pop(0)) #Joga o primeiro elemento da lista pro final

def deadEndRelease(sondaTemp,hops):
    #RELEASE OVERHEAD MPINT
    overhead_DataPlane_MPINT.append(overhead_MPINT_Temp.copy())
    overhead_ControlPlane_MPINT.append(calculaOverheadMPINT(len(sondaTemp)+1,hops))
    overhead_MPINT_Temp.clear()

    #RELEASE OVERHEAD MPOLKA
    overhead_DataPlane_MPolkaCRC8.append(overhead_MPolkaCRC8_Temp.copy())
    overhead_DataPlane_MPolkaCRC16.append(overhead_MPolkaCRC16_Temp.copy())
    overheadCRC8, overheadCRC16 = calculaOverheadMPolka(len(sondaTemp)+1)
    overhead_ControlPlane_MPolkaCRC8.append(overheadCRC8)
    overhead_ControlPlane_MPolkaCRC16.append(overheadCRC16)
    overhead_MPolkaCRC8_Temp.clear()
    overhead_MPolkaCRC16_Temp.clear()

    #RELEASE OVERHEAD INT CLASSICO
    sendNewProbe(hops) #Caso precise replicar, ele envia uma nova sonda.
    overhead_DataPlane_INTClassico.append(overhead_INTClassico_Temp.copy())
    overhead_ControlPlane_INTClassico.append(calculaOverheadINTClassico(hops))
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

def extractMPolkaOverhead():
    overheadDP = sum(sum(overhead_DataPlane_MPolkaCRC16,[]))
    overheadCP = sum(overhead_ControlPlane_MPolkaCRC16)
    return overheadDP,overheadCP

def extractReplication():
    return replication