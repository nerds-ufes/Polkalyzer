import networkx as nx
import lib.outputValidator as ov
from mininet.net import Mininet
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import subprocess

def userInputToConfig(rawInput):
    customConfig = {}
    for item in rawInput.split(","):
        key, value = item.split("=")
        customConfig[key.strip()] = value.strip()
    config_str = ",".join([f"{key}:{value}" for key, value in customConfig.items()])
    return customConfig

def customizeComponent(topologyName,linePrefix,componentNumber):
    #pathToImage = ov.toUniversalOSPath(f'output/Topology/{topologyName}/draw/TopologyNX.png')
    #fsubprocess.run(['gwenview',pathToImage])
    if(linePrefix == 's'):
        print('Type your comma separated SWITCH config, like (cls=OVSSwitch,ip=10.0.0.1):')
        userInput = input()
    elif(linePrefix == 'lss'):
        print('Type your comma separated LINK config, like (bw=100, delay:3, loss: 12):')
        userInput = input()

    customConfig = userInputToConfig(userInput)

    prefix_map = {
        's': '**switchParameters',
        'lss': '**linkSSParameters',
    }

    if(ov.isFile(f'output/CustomMininetNX/{topologyName}.py')):
        customLine = f'custom_{linePrefix}{componentNumber}'
        with open(ov.toUniversalOSPath(f'output/CustomMininetNX/{topologyName}.py'),'r') as arq:
            lines = arq.readlines()
            lineNumber = 0
            alreadyCustomized = False
            for line in lines:
                if customLine in line:
                    alreadyCustomized = True
            if(alreadyCustomized): # Component Already Customized
                for line in lines:
                    if(f'{customLine} =' in line):
                        myLine = lineNumber
                    lineNumber += 1
                lines[myLine] = f'\t\t{customLine} = {customConfig}\n'
            else: # Component Not Customized
                for line in lines:
                    if(line == "\t\t#Custom Parameters\n"):
                        myFirstLine = lineNumber
                    if(f'{linePrefix}{componentNumber} = ' in line):
                        mySecondLine = lineNumber
                    lineNumber += 1

                lines[myFirstLine] = f"\t\t#Custom Parameters\n\t\t{customLine} = {customConfig}\n"
                lines[mySecondLine] = lines[mySecondLine].replace(prefix_map[linePrefix],f'**{customLine}')

        with open(ov.toUniversalOSPath(f'output/CustomMininetNX/{topologyName}.py'),'w') as arq:
            arq.writelines(lines)

def createCustomTopology(topologyName):
    if(ov.isFile(f'output/CustomMininetNX/{topologyName}.py')):
        if(not ov.isFile("output/CustomMininetNX/Makefile")):
            createMakeFile('output/CustomMininetNX')
        return 1

    with open(ov.toUniversalOSPath(f'output/MininetNX/{topologyName}.py'),'r') as arq:
        lines = arq.readlines()
        lineNumber = 0
        for line in lines:
            if(line == "\t\t#Add Switches\n"):
                myLine = lineNumber
            lineNumber += 1
        lines[myLine] = "\t\t#Custom Parameters\n\t\t#Add Switches\n"

    createMakeFile('output/CustomMininetNX')

    with open(ov.toUniversalOSPath(f'output/CustomMininetNX/{topologyName}.py'),'w') as arq:
        arq.writelines(lines)

def displayCustomizedComponents(topologyName):
    # Mapeamento de strings de entrada para strings de saída correspondentes
    string_map = {
        '\t\tcustom_lss': 'Link SS',
        '\t\tcustom_lhs': 'Link HS',
        '\t\tcustom_s': 'Switch',
        '\t\tcustom_h': 'Host'
    }
    # Abrir o arquivo para leitura
    with open(ov.toUniversalOSPath(f'output/CustomMininetNX/{topologyName}.py'),'r') as arq:
        # Ler cada linha do arquivo
        for line in arq:
            # Verificar se a linha contém uma das strings de entrada
            for key in string_map.keys():
                if key in line:
                    # Extrair o número do link a partir da linha
                    link = int(line.split(key)[1].split()[0])
                    # Usar eval() para criar um dicionário a partir da string
                    d = eval(line.split('=')[1])
                    # Criar uma lista de strings formatadas para cada chave-valor do dicionário
                    params = [f"{key}: {value}" for key, value in d.items()]
                    # Concatenar os itens da lista em uma única string
                    params_str = " | ".join(params)
                    # Obter a string de saída correspondente
                    output_key = key
                    output_str = string_map[output_key]
                    # Formatar a saída com base nos valores do dicionário, do link e da string de saída correspondente
                    output = f"{output_str} {link} -> {params_str}"
                    # Imprimir a saída
                    print(output)

def networkxToMininet(G,hostsPerSwitch):
    net = Mininet()
    # Construct mininet
    for n in G.nodes:
        net.addSwitch("s_%s" % n)
        # Add single host on designated switches
        if int(n) in hostsPerSwitch:
            net.addHost("h%s" % n)
            # directly add the link between hosts and their gateways
            net.addLink("s_%s" % n, "h%s" % n)
    # Connect your switches to each other as defined in networkx graph
    for (n1, n2) in G.edges:
        net.addLink('s_%s' % n1,'s_%s' % n2)
    return net

def networkxToMininetConfig(G,topologyName,hostsPerSwitch):
    Code = ""
    Import= "from mininet.topo import Topo\n"+\
            "from mininet.net import Mininet\n"+\
            "from mininet.cli import CLI\n"+\
            "from mininet.link import TCLink\n"+\
            "from mininet.log import info,setLogLevel\n\n"
    Class =f"class MininetNX( Topo ):\n\t"+\
                "def build( self ):\n\t\t"
    DefaultParameters = "#Set Here Default Parameters\n\t\t"+\
                        "switchParameters= {}\n\t\t"+\
                        "hostParameters= {}\n\t\t"+\
                        "linkHSParameters= {}\n\t\t"+\
                        "linkSSParameters= {}\n\t\t"
    
    SwitchConfig = "#Add Switches\n\t\t"
    HostConfig = f"#Add {hostsPerSwitch} hosts to each switch\n\t\t"
    HostSwitchLinkConfig = "#Add a link of hosts and switch\n\t\t"
    SwitchSwitchLinkConfig = "#Add a link of switches of original topology\n\t\t"
    StartNetwork = f"\ndef startNetwork():"+\
                        "\n\ttopo = MininetNX()"+\
                        "\n\tnet = Mininet(topo=topo, autoSetMacs=True, link=TCLink)"+\
                        "\n\tnet.start()"+\
                        "\n\tCLI(net)"
    BuildTopo = f"\n\nif __name__ == '__main__':"+\
                    "\n\tsetLogLevel( 'info' )"+\
                    "\n\tstartNetwork()"

    h = 0 # Host Number
    for s in G.nodes:
        SwitchConfig += f"s{s} = self.addSwitch('s{s}',**switchParameters)\n\t\t"
        # Add single host on designated switches
        for cont in range(hostsPerSwitch):
            HostConfig += f"h{h} = self.addHost('h{h}',**hostParameters)\n\t\t"
            # directly add the link between hosts and their gateways
            HostSwitchLinkConfig += f"lhs{h} = self.addLink('s{s}','h{h}',**linkHSParameters)\n\t\t"
            h += 1
    # Connect your switches to each other as defined in networkx graph
    l = 0 #Link Switch Switch
    for (s1, s2) in G.edges:
        SwitchSwitchLinkConfig += f"lss{l} = self.addLink('s{s1}','s{s2}',**linkSSParameters)\n\t\t"
        l+=1
    
    Code = Code.join([Import,Class,DefaultParameters,SwitchConfig,HostConfig,HostSwitchLinkConfig,SwitchSwitchLinkConfig,StartNetwork,BuildTopo])
    
    with open(ov.toUniversalOSPath(f'output/MininetNX/{topologyName}.py'),'w') as arq:
        arq.write(Code)

    createMakeFile('output/MininetNX') # Command: make <TopologyName>

def createMakeFile(path): # Temporary solution, this function will be a shell script or a better solution
    ov.validateEntirePath(path)
    with open(ov.toUniversalOSPath(f'{path}/Makefile'),'w') as arq:
        arq.write("%:\n\t@sudo mn --custom $*.py --topo $*")