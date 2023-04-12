import networkx as nx
import lib.outputValidator as ov
from mininet.net import Mininet

def extractLine(topologyName,linePrefix,lineNumber):
    with open(ov.toUniversalOSPath(f'output/MininetNX/{topologyName}.py'),'r') as arq:
        lines = arq.readlines()
        for line in lines:
            if(f'{linePrefix}{lineNumber}' in line):
                print('Your line is: ', line)
                return line
            
def customizeLink(myDict):
    print('customizing link')
    #r1r2 = {'bw':100,'delay':'3','loss':12}.

def importConfigs():
    print('My custom config')

def exportConfigs():
    print('My custom config')

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
    Import = "from mininet.topo import Topo\n\n"
    Class = f"class MininetNX( Topo ):\n\tdef build( self ):\n\t\t"

    SwitchConfig = "#Add Switches\n\t\t"
    HostConfig = f"#Add {hostsPerSwitch} hosts to each switch\n\t\t"
    HostSwitchLinkConfig = "#Add a link of hosts and switch\n\t\t"
    SwitchSwitchLinkConfig = "#Add a link of switches of original topology\n\t\t"
    BuildTopo = f"\ntopos = {{ '{topologyName}': ( lambda: MininetNX() ) }}"

    h = 0 # Host Number
    for s in G.nodes:
        SwitchConfig += f"s{s} = self.addSwitch('s{s}')\n\t\t"
        # Add single host on designated switches
        for cont in range(hostsPerSwitch):
            HostConfig += f"h{h} = self.addHost('h{h}')\n\t\t"
            # directly add the link between hosts and their gateways
            HostSwitchLinkConfig += f"lhs{h} = self.addLink('s{s}','h{h}')\n\t\t"
            h += 1
    # Connect your switches to each other as defined in networkx graph
    l = 0 #Link Switch Switch
    for (s1, s2) in G.edges:
        SwitchSwitchLinkConfig += f"lss{l} = self.addLink('s{s1}','s{s2}')\n\t\t"
        l+=1
    
    Code = Code.join([Import,Class,SwitchConfig,HostConfig,HostSwitchLinkConfig,SwitchSwitchLinkConfig,BuildTopo])
    
    with open(ov.toUniversalOSPath(f'output/MininetNX/{topologyName}.py'),'w') as arq:
        arq.write(Code)

    createMakeFile() # Command: make <TopologyName>

def createMakeFile(): # Temporary solution, this function will be a shell script or a better solution
    with open(ov.toUniversalOSPath(f'output/MininetNX/Makefile'),'w') as arq:
        arq.write("%:\n\t@sudo mn --custom $*.py --topo $*")