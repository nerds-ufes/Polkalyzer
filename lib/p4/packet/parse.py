import struct
import socket
import redis

class parse():
    def filter(self, pkt_raw):  # filter int packet
        red_path = redis.Redis(unix_socket_path='/var/run/redis/redis-server.sock',db=1)
        red_int = redis.Redis(unix_socket_path='/var/run/redis/redis-server.sock',db=4)

        pkt_len = len(pkt_raw)
        pkt = struct.unpack("!14s%ds" % (pkt_len - 14), pkt_raw)
        ethernet = self.parse_ethernet(pkt[0])
        if ethernet == 8224:
            pkt = struct.unpack("!20s%ds" % (pkt_len - 14 - 20), pkt[1])
            id_as_key = self.parse_ipv4(pkt[0])

            pkt = struct.unpack("!B%ds" % (pkt_len - 14 - 20 - 1), pkt[1])
            path_option = pkt[0]
            pkt_remain = pkt[1]
            if path_option != 0:
                pkt_remain = self.path_pro(red_path, path_option, id_as_key, pkt[1])

            pkt_remain_len = len(pkt_remain)
            pkt = struct.unpack("!B%ds" % (pkt_remain_len - 1), pkt_remain)
            int_option = pkt[0]
            if int_option != 0:
                data = self.int_pro(red_int, int_option, pkt[1])
                return data

        else:
            return False

    def int_pro(self, red_int, n, pkt_raw):
        pkt_len = len(pkt_raw)
        int_list = []
        fmt = "!"
        for i in range(n):
            fmt = fmt + "32s"

        pkt = struct.unpack("%s%ds" % (fmt, pkt_len - n * 32), pkt_raw)

        for i in range(n):
            int_info = self.parse_int(red_int, pkt[i])
            int_list.append(int_info)

        return int_list

    def path_pro(self, red_path, n, id_as_key, pkt_raw):
        pkt_len = len(pkt_raw)
        path_list = []
        fmt = "!"
        for i in range(n):
            fmt = fmt + "s"

        pkt = struct.unpack("%s%ds" % (fmt, pkt_len - n * 1), pkt_raw)

        for i in range(n):
            path_info = self.parse_path(pkt[i])
            path_list.append(path_info)

        self.writeRedis(red_path, path_list, id_as_key)

        return pkt[n]

    def parse_path(self, pkt):
        pathhdr = struct.unpack("!B", pkt)
        sw_id = pathhdr[0]
        return sw_id

    def writeRedis(self, red_path, int_path_sw_id_list, id_as_key):
        key = id_as_key
        red_path.hset("mul",key, "")
        s = ""
        for item in int_path_sw_id_list:
            s = s + str(item) + ","

        s = s[0: len(s)-1]
        red_path.sadd(key, s)

	# B: unsigned char 1B; H: unsigned short 2B; I: unsigned int 4B

    def parse_int(self, red_int, pkt):
        inthdr = struct.unpack("!BBBBIHIHIsHBIsHB", pkt)
        sw_id = inthdr[0]
        ingress_port = inthdr[1]
        egress_port = inthdr[2]
        replicate_count = inthdr[3]
        egress_global_tstamp = (inthdr[4] << 16) + inthdr[5]
        enq_qdepth = (inthdr[10] << 8) + inthdr[11]
        deq_qdepth = (inthdr[-2] << 8) + inthdr[-1]
        time_delta = inthdr[-4]
        str_int = "sw_id:%s|ingress_port:%s|egress_port:%s|egress_global_tstamp:%s|enq_qdepth:%s|deq_qdepth:%s|time_delta:%s|rep_count:%s" \
        % (sw_id,ingress_port,egress_port,egress_global_tstamp,enq_qdepth,deq_qdepth,time_delta,replicate_count)
        red_int.set(sw_id, str_int)
        return str_int

    def parse_ethernet(self, pkt):
        ethernet = struct.unpack("!6B6BH", pkt)
        ethernet_str = []
        for i in range(12):
            temp = ethernet[i]
            temp = (hex(temp))[2:]
            if len(temp) == 1:
                temp = "0" + temp
            ethernet_str.append(temp)

        '''
        dstAddr = "%s:%s:%s:%s:%s:%s" % (
            ethernet_str[0], ethernet_str[1], ethernet_str[2], ethernet_str[3], ethernet_str[4], ethernet_str[5])  # 1
        srcAddr = "%s:%s:%s:%s:%s:%s" % (
            ethernet_str[6], ethernet_str[7], ethernet_str[8], ethernet_str[9], ethernet_str[10], ethernet_str[11])  # 2
        '''
        etherType = ethernet[12]  # 3

        return etherType

    def parse_ipv4(self, pkt):
        ipv4 = struct.unpack("!BBHHHBBH4s4s", pkt)
        version = (ipv4[0] & 0xf0) >> 4  # 1
        ihl = ipv4[0] & 0x0f  # 2
        diffserv = ipv4[1]  # 3
        totalLen = ipv4[2]  # 4
        identification = ipv4[3]  # 5
        flags = (ipv4[4] & 0xe000) >> 13  # 6
        fragOffset = ipv4[4] & 0x1fff  # 7
        ttl = ipv4[5]  # 8
        protocol = ipv4[6]  # 9
        hdrChecksum = ipv4[7]  # 10
        srcAddr = ipv4[8]  # 11
        dstAddr = ipv4[9]  # 12
        srcAddr = socket.inet_ntoa(srcAddr)
        dstAddr = socket.inet_ntoa(dstAddr)
        id_as_key = str(identification)
        return id_as_key

if __name__ == "__main__":
    pass
