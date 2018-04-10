import struct
from .static import IP_PROTOCOL
from .underIP import *
class IP(object):
    def __init__(self,other_data):
        self.raw_data = other_data
        self.analysis()

    # def input_data(self, other_data):
    #     self.raw_data = other_data

    def get_protocol(self, num_pro):
        try:
            return IP_PROTOCOL[num_pro]
        except:
            print("ERROR")

    def analysis(self):
        VER_IHL, DS_ECN, self.TOTALEN, self.IDENT, FLAG_OFFSET, self.TTL, PRC, self.CHECKSUM, src, dest= struct.unpack('B B H H H B B H 4s 4s', self.raw_data[:20])
        self.VER, self.IHL = self.get_ver_IHL(VER_IHL)
        self.DS, self.ECN = self.get_DS_ECN(DS_ECN)
        self.FLAG, self.OFFSET = self.get_FG_OFF(FLAG_OFFSET)
        self.PROTOCOL = self.get_protocol(num_pro = PRC)
        self.SRC_IP4 = self.get_IP4_addr(src)
        self.DEST_IP4 = self.get_IP4_addr(dest)
        
        if self.IHL > 5:
            self.option = self.raw_data[20:self.IHL*4]
        else:
            self.option = None

        self.other_data = self.raw_data[self.IHL*4:]
        
    def get_ver_IHL(self, VER_IHL):
        IHL = VER_IHL & 0x0F
        VER = VER_IHL >> 4
        return (VER, IHL)

    def get_DS_ECN(self, DS_ECN):
        DS = DS_ECN >> 2
        ECN = DS_ECN & 0x03
        return (DS, ECN)

    def get_FG_OFF(self, FLAG_OFFSET):
        OFFSET = FLAG_OFFSET & 0x1F
        FLAG = FLAG_OFFSET >> 13
        return (FLAG, OFFSET)

    def get_IP4_addr(self, IPaddr):
        byte_str = map('{:02d}'.format, IPaddr)
        Ip_addr = ':'.join(byte_str)
        return Ip_addr

    def print_result(self):
        print('Destination: {}, Source: {}, Protocol: {}'.format(self.DEST_IP4, self.SRC_IP4, self.PROTOCOL))

    def deal_data(self):
        if self.PROTOCOL == 'ICMP':
            '''互联网控制消息协议'''
            return ICMP(self.other_data)
        # elif self.PROTOCOL == 'IGMP':
        #     '''互联网组管理协议'''
        #     pass
        elif self.PROTOCOL == 'TCP':
            '''传输控制协议'''
            return TCP(self.other_data)
        elif self.PROTOCOL == 'UDP':
            '''用户数据报协议'''
            return UDP(self.other_data)
        elif self.PROTOCOL == 'SCTP':
            '''流控制传输协议'''
            pass
        else:
            '''仅识别 不分析'''
            pass
