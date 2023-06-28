#!/usr/bin/env python

from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel, info
from mininet.cli import CLI

from p4_mininet import P4Switch, P4Host

import argparse
import os
from time import sleep

parser = argparse.ArgumentParser(description='Mininet demo')
parser.add_argument('--behavioral-exe', help='Path to behavioral executable',
                    type=str, action="store", default="/home/p4/INTMPolKA/behavioral-model/targets/simple_switch/simple_switch")
parser.add_argument('--thrift-port', help='Thrift server port for table updates',
                    type=int, action="store", default=9090)
#parser.add_argument('--json', help='Path to JSON config file',
#                    type=str, action="store", required=False)
parser.add_argument('--pcap-dump', help='Dump packets on interfaces to pcap files',
                    type=str, action="store", required=False, default=False)

args = parser.parse_args()


class INTTopo(Topo):
    "Single switch connected to n (< 256) hosts."
    def __init__(self, sw_path, thrift_port, pcap_dump, n, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        self.switch_list = []
        self.host_list = []

        #Switch de borda
        info("*** Adding P4Switches (edge)\n")
        e = 4
        for h in xrange(e):
            switch = self.addSwitch('e%d' % (h + 1),
                                    sw_path = sw_path,
                                    json_path = "/home/p4/INTMPolKA/topo_unknown/multi_mc/m-polka-int-edge.json",
                                    thrift_port = thrift_port,
                                    pcap_dump = pcap_dump,
                                    log_console = True)
            self.switch_list.append(switch)
            thrift_port = thrift_port + 1

        #Switch core
        info("*** Adding P4Switches (core)\n")
        m = 7
        for h in xrange(m):
            switch = self.addSwitch('s%d' % (h + 1),
                                    sw_path = sw_path,
                                    json_path = "/home/p4/INTMPolKA/topo_unknown/multi_mc/mpint_topo_unknown_multi_mc.json",
                                    thrift_port = thrift_port,
                                    pcap_dump = pcap_dump,
                                    log_console = True)
            self.switch_list.append(switch)
            thrift_port = thrift_port + 1

        info("*** Adding hosts\n")
        n = 4
        for h in xrange(n):
            host = self.addHost('h%d' % (h + 1),
                                ip = "10.0.1.%d/24" % (h+1),
                                mac = '00:04:00:00:00:%02x' %h)
            self.host_list.append(host)

        self.addLink(self.host_list[0], self.switch_list[0])    #h1-e1
        self.addLink(self.switch_list[0], self.switch_list[4])  #e1-s1
        self.addLink(self.switch_list[4], self.switch_list[8])  #s1-s5
        self.addLink(self.switch_list[4], self.switch_list[5])  #s1-s2
        self.addLink(self.switch_list[5], self.switch_list[9])  #s2-s6
        self.addLink(self.switch_list[9], self.switch_list[7])  #s6-s4
        self.addLink(self.switch_list[7], self.switch_list[2])  #s4-e3
        self.addLink(self.switch_list[2], self.host_list[2])    #e3-h3
        self.addLink(self.switch_list[9], self.switch_list[10]) #s6-s7
        self.addLink(self.switch_list[10], self.switch_list[3]) #s7-e4
        self.addLink(self.switch_list[3], self.host_list[3])    #e4-h4
        self.addLink(self.switch_list[8], self.switch_list[6])  #s5-s3
        self.addLink(self.switch_list[6], self.switch_list[1])  #s3-e2
        self.addLink(self.switch_list[1], self.host_list[1])    #e2-h2

def main():
    num_hosts = 4

    topo = INTTopo(args.behavioral_exe,
                   #args.json,
                   args.thrift_port,
                   args.pcap_dump,
                   num_hosts)
    net = Mininet(topo = topo,
                  host = P4Host,
                  switch = P4Switch,
                  controller = None)
    net.start()
    net.staticArp()

    os.system("../flow_table/f.sh")

    for n in xrange(num_hosts):
        h = net.get('h%d' % (n + 1))
        h.describe()
        if n != 0:
            h.cmd("ethtool --offload eth0 rx off tx off")
            h.cmd("python2 ../packet/receive.py >/dev/null &")
            h.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
            h.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
            h.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")


    for sw in net.switches:
        sw.cmd("sysctl -w net.ipv6.conf.all.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.default.disable_ipv6=1")
        sw.cmd("sysctl -w net.ipv6.conf.lo.disable_ipv6=1")

    sleep(1)

    print "Ready !"

    CLI( net )
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    main()
