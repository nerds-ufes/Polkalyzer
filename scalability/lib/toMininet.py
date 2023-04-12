import networkx as nx
from mininet.net import Mininet

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
            h += 1
            HostConfig += f"h{h} = self.addHost('h{h}')\n\t\t"
            # directly add the link between hosts and their gateways
            HostSwitchLinkConfig += f"self.addLink('s{s}','h{h}')\n\t\t"
    # Connect your switches to each other as defined in networkx graph
    for (s1, s2) in G.edges:
        SwitchSwitchLinkConfig += f"self.addLink('s{s1}','s{s2}')\n\t\t"
    
    Code = Code.join([Import,Class,SwitchConfig,HostConfig,HostSwitchLinkConfig,SwitchSwitchLinkConfig,BuildTopo])
    
    with open(f'output/MininetNX/{topologyName}.py','w') as arq:
        arq.write(Code)

    createMakeFile() # Command: make <TopologyName>

def createMakeFile(): # Temporary solution, this function will be a shell script or a better solution
    with open(f'output/MininetNX/Makefile','w') as arq:
        arq.write("%:\n\t@sudo mn --custom $*.py --topo $*")