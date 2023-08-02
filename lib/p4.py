import toml
from pathlib import Path
import lib.outputValidator as ov

def networkx_to_mininet_P4(T,topologyName): # T is the MST of the topology
    # Read informations from toml file
    topology = toml.load(Path(f"output/Topology/{topologyName}/topology.toml"))

    edgeSwitches = topology['mpolka']['edgeSwitches']
    number_of_coreSwitches = topology['mpolka']['number_of_coreSwitches']
    number_of_edgeSwitches = topology['mpolka']['number_of_edgeSwitches']
    number_of_hosts = number_of_edgeSwitches
    
    Code = ""
    CompilerDirective = "#!/usr/bin/env python\n\n"
    Import= "from mininet.topo import Topo\n"+\
            "from mininet.net import Mininet\n"+\
            "from mininet.cli import CLI\n"+\
            "from mininet.link import TCLink\n"+\
            "from mininet.log import info,setLogLevel\n"+\
            "from lib.p4.p4_mininet import P4Switch, P4Host\n\n"+\
            "import argparse\n"+\
            "import os\n"+\
            "from time import sleep\n\n"
    ArgParser = "parser = argparse.ArgumentParser(description='Mininet demo')\n"+\
                "parser.add_argument('--behavioral-exe', help='Path to behavioral executable',\n"+\
                "\t\t\t\t\ttype=str, action=\"store\", default=\"../../../lib/p4/behavioral-model/targets/simple_switch/simple_switch\")\n"+\
                "parser.add_argument('--thrift-port', help='Thrift server port for table updates',\n"+\
                "\t\t\t\t\ttype=int, action=\"store\", default=9090)\n"+\
                "#parser.add_argument('--json', help='Path to JSON config file',\n"+\
                "#\t\t\t\t\ttype=str, action=\"store\", required=False)\n"+\
                "parser.add_argument('--pcap-dump', help='Dump packets on interfaces to pcap files',\n"+\
                "\t\t\t\t\ttype=str, action=\"store\", required=False, default=False)\n\n"+\
                "args = parser.parse_args()\n\n"
    Class =f"class INTTopo( Topo ):\n\t"+\
                '"Single switch connected to n (< 256) hosts."\n\t'+\
                "def __init__(self, sw_path, thrift_port, pcap_dump, n, **opts):\n\t\t"+\
                "Topo.__init__( self, **opts )\n"
    EdgeSwitchConfig = "\n\t\tinfo('*** Adding P4Switches (edge)\\n')\n\t\t"+\
                        f"e = {number_of_edgeSwitches}\n\t\t"+\
                        "for h in xrange(e):\n\t\t\t"+\
                            "switch = self.addSwitch('e%d' % (h + 1),\n\t\t\t\t"+\
                                    "sw_path = sw_path,\n\t\t\t\t"+\
                                    f"json_path = '../../../lib/p4/mpolka-int-edge.json',\n\t\t\t\t"+\
                                    "thrift_port = thrift_port,\n\t\t\t\t"+\
                                    "pcap_dump = pcap_dump,\n\t\t\t\t"+\
                                    "log_console = True)\n\t\t\t"+\
                            "thrift_port = thrift_port + 1\n"
    CoreSwitchConfig = "\n\t\tinfo('*** Adding P4Switches (core)\\n')\n\t\t"+\
                        f"m = {number_of_coreSwitches}\n\t\t"+\
                        "for h in xrange(m):\n\t\t\t"+\
                            "switch = self.addSwitch('c%d' % (h + 1),\n\t\t\t\t"+\
                                    "sw_path = sw_path,\n\t\t\t\t"+\
                                    f"json_path = '../../../lib/p4/mpolka-int-core.json',\n\t\t\t\t"+\
                                    "thrift_port = thrift_port,\n\t\t\t\t"+\
                                    "pcap_dump = pcap_dump,\n\t\t\t\t"+\
                                    "log_console = True)\n\t\t\t"+\
                            "thrift_port = thrift_port + 1\n"
    HostConfig = f"\n\t\tinfo('*** Adding hosts\\n')\n\t\t"+\
                    f"n = {number_of_hosts}\n\t\t"+\
                    "for h in xrange(n):\n\t\t\t"+\
                        "host = self.addHost('h%d' % (h + 1),\n\t\t\t\t"+\
                                "ip = '10.0.%d.1/24' % (h + 1),\n\t\t\t\t"+\
                                "mac = '00:00:00:00:00:%02x' % (h + 1))\n"
    #Link each host to respective edge switch
    HostSwitchLinkConfig = "\n\t\tinfo('*** Creating links between hosts and edge switches\\n')\n\t\t"+\
                            "for h in xrange(n):\n\t\t\t"+\
                                "self.addLink('h%d' % (h + 1), 'e%d' % (h + 1))\n"
    #Link link edge switches(e1,e2,...) to core switches (ci,cj,..., i,j <= m)
    ESwitchCSwitchLinkConfig = "\n\t\tinfo('*** Creating links between edge and core switches\\n')\n\t\t"
    for e in range(number_of_edgeSwitches):
        ESwitchCSwitchLinkConfig += f"self.addLink('e{e}', 'c{edgeSwitches[e]}')\n\t\t"
    #Link between core switches
    CSwitchCSwitchLinkConfig = "\n\t\tinfo('*** Creating links between core switches\\n')\n\t\t"
    for (s1,s2) in T.edges:
        CSwitchCSwitchLinkConfig += f"self.addLink('c{s1}', 'c{s2}')\n\t\t"

    StartNetwork = f"num_hosts = {number_of_hosts}\n\t"+\
                    "topo = INTTopo(args.behavioral_exe,\n\t\t\t\t"+\
                    f"args.thrift_port,\n\t\t\t\t"+\
                    f"args.pcap_dump,\n\t\t\t\t"+\
                    f"num_hosts)\n\t"+\
                    "net = Mininet(topo = topo,\n\t\t\t\t"+\
                    "host = P4Host,\n\t\t\t\t"+\
                    "switch = P4Switch,\n\t\t\t\t"+\
                    "controller = None)\n\n\t"+\
                    "net.start()\n\t"+\
                    "net.staticArp()\n\t"+\
                    f"os.system('output/Topology/{topologyName}/p4/flow_table/f.sh {number_of_edgeSwitches} {number_of_coreSwitches}')\n\n\t"

    ConfigNetwork = "for n in xrange(num_hosts):\n\t\t"+\
                        "h = net.get('h%d' % (n + 1))\n\t\t"+\
                        "h.describe()\n\t\t"+\
                        "if n != 0:\n\t\t\t"+\
                            "h.cmd('ethtool --offload eth0 rx off tx off')\n\t\t\t"+\
                            "h.cmd('python2 ../packet/receive.py >/dev/null &')\n\t\t\t"+\
                            "h.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')\n\t\t\t"+\
                            "h.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')\n\t\t\t"+\
                            "h.cmd('sysctl -w net.ipv6.conf.lo.disable_ipv6=1')\n\n\t\t"+\
                    "for sw in net.switches:\n\t\t\t"+\
                        "sw.cmd('sysctl -w net.ipv6.conf.all.disable_ipv6=1')\n\t\t\t"+\
                        "sw.cmd('sysctl -w net.ipv6.conf.default.disable_ipv6=1')\n\t\t\t"+\
                        "sw.cmd('sysctl -w net.ipv6.conf.lo.disable_ipv6=1')\n\n\t\t"+\
                    "sleep(1)\n\n\t"+\
                    "print 'Ready !'\n\n\t"+\
                    "CLI( net )\n\t"+\
                    "net.stop()\n\n"

    Main = "\ndef main():\n\t" + StartNetwork + ConfigNetwork + "\n"

    BuildTopo = f"\nif __name__ == '__main__':"+\
                    "\n\tsetLogLevel( 'info' )"+\
                    "\n\tmain()"

    Code = Code.join([CompilerDirective,
                      Import,
                      ArgParser,
                      Class,
                      EdgeSwitchConfig,
                      CoreSwitchConfig,
                      HostConfig,
                      HostSwitchLinkConfig,
                      ESwitchCSwitchLinkConfig,
                      CSwitchCSwitchLinkConfig,
                      Main,
                      BuildTopo])

    with open(Path(f'output/Topology/{topologyName}/{topologyName}-P4.py'),'w') as arq:
        arq.write(Code)

    createFlowTable(T,topologyName)

def createFlowTable(T,topologyName):
    ov.validateEntirePath(f'output/Topology/{topologyName}/flow_table')

    topology = toml.load(Path(f"output/Topology/{topologyName}/topology.toml"))

    edgeSwitches = topology['mpolka']['edgeSwitches']
    number_of_edgeSwitches = topology['mpolka']['number_of_edgeSwitches']
    nodesID = topology['mpolka']['nodesID']
    routeID = topology['mpolka']['routeID']

    print(topologyName)

    for e in range(number_of_edgeSwitches):
        with open(Path(f'output/Topology/{topologyName}/flow_table/e{e+1}.txt'),'w') as arq:
            arq.write('table_set_default tunnel_encap_process_sr tdrop\n')
            arq.write(f'table_add tunnel_encap_process_sr add_sourcerouting_header 10.0.1.{e+1}/32 => {e+1} 1 00:04:00:00:00:{e:02x} {hex(routeID[str(edgeSwitches[e])])}\n\n')
    
    print(T.degree())
    print(f'nodesID: {len(nodesID)}')
    for c, degree in T.degree():
        if(c not in edgeSwitches):
            degree=degree-1 # Core Switches connected to edge switches don't decrease the degree
        with open(Path(f'output/Topology/{topologyName}/flow_table/s{c+1}.txt'),'w') as arq:
            arq.write(f'table_add addIntInfo add_int_info 0x2020 => {c+1} {degree}\n\n')
            arq.write(f'set_crc16_parameters calc {nodesID[c]} 0x0 0x0 false false\n')
            arq.write('mirroring_add 1 1\n')
            arq.write('mirroring_add 2 2\n')
            arq.write('mirroring_add 3 3\n')
