import struct
import sys
from .underIP import *
sys.path.append("..")
from common import get_IP4_addr, IP_PROTOCOL

class IP(object):
    def __init__(self,other_data):
        self.raw_data = other_data
        self.__analysis()

    # def input_data(self, other_data):
    #     self.raw_data = other_data

    def get_protocol(self, num_pro):
        try:
            return IP_PROTOCOL[num_pro]
        except:
            print("ERROR")

    def __analysis(self):
        VER_IHL, DS_ECN, self.TOTALEN, self.IDENT, FLAG_OFFSET, self.TTL, PRC, self.CHECKSUM, src, dest= struct.unpack('! B B H H H B B H 4s 4s', self.raw_data[:20])
        self.VER, self.IHL = self.get_ver_IHL(VER_IHL)
        self.DS, self.ECN = self.get_DS_ECN(DS_ECN)
        self.FLAG, self.OFFSET = self.get_FG_OFF(FLAG_OFFSET)
        self.PROTOCOL = self.get_protocol(num_pro = PRC)
        self.SRC_IP4 = get_IP4_addr(src)
        self.DEST_IP4 = get_IP4_addr(dest)
        
        if self.IHL > 5:
            self.option = self.raw_data[20:self.IHL*4]
        else:
            self.option = None

        self.other_data = self.raw_data[self.IHL*4:]

    def print_result(self):
        print('Destination: {}, Source: {}, Protocol: {}'.format(self.DEST_IP4, self.SRC_IP4, self.PROTOCOL))

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

    def get_IP(self):
        return (str(self.SRC_IP4), str(self.DEST_IP4))
    
    def get_Info(self):
        info = {}
        info['version'] = '[4 bit]' + str(self.VER)
        info['Internet head lenth'] = '[4 bit]' + str(self.IHL)
        info['Diff_service'] = '[6 bit]' + str(self.DS)
        info['ECN'] = '[2 bit]' + str(self.ECN)
        info['total_length'] = '[16 bit]' + str(self.TOTALEN)
        info['identification'] = '[16 bit]' + str(self.IDENT)
        info['flags'] = '[3 bit]' + str(self.FLAG)
        info['offset'] = '[13 bit]' + str(self.OFFSET)
        info['TTL'] = '[8 bit]' + str(self.TTL)
        info['IPv4_protocol'] = '[8 bit]' + str(self.PROTOCOL)
        info['checksum'] = '[16 bit]' + str(self.CHECKSUM)
        info['SRC_IPv4'] = '[32 bit]' + str(self.SRC_IP4)
        info['DEST_IPv4'] = '[32 bit]' + str(self.DEST_IP4)

        return (info, 'IP')

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
            return SCTP(self.other_data)
        else:
            '''仅识别 不分析'''
            pass
