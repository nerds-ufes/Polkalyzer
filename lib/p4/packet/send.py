#!/usr/bin/env python
import sys
import time
import random
from int_hdrs import *

def main():
    identification=random.randint(1,65535)

    iface = 'h0-eth0'

    pkt =  Ether(dst='00:aa:bb:00:00:00', src=get_if_hwaddr('eth0'), type=8224);
    try:
        pkt = pkt / SourceRoute(nrouteid=1915945086214166489341648836749912) #borda so faz essa linha - alem do routeID, inserir o cabecalho INT
    except ValueError:
        pass

    pkt = pkt / IP(id=identification)/IntHeader(ver=2, d=0, e=0, m=0, r=0, hop_ml=10, remaining_hop_count=0, instruction_bitmap=56832, domain_specific_id=0x0000)

    try:
        pkt.show2()
        time.sleep(1)
        sendp(pkt, iface='eth0')
        time.sleep(1)
    except KeyboardInterrupt:
        sys.exit()

if __name__ == '__main__':
    main()
