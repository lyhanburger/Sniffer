import struct
from .underIP import *
sys.path.append("..")
from common import get_IP6_addr, IP_PROTOCOL
def get_ver_TC_QOS(ver_TC_QOS):
    ver = ver_TC_QOS >> 28
    qos = ver_TC_QOS & 0x000fffff
    tc = (ver_TC_QOS >> 20) & 0x000000ff
    return(ver, qos, tc)

class IPv6(object):
    """docstring for IPv6"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        ver_TC_QOS, self.PAYLOAD_LEN, nexthead, self.HOPLIMIT, src, dest= struct.unpack('! I H B B 16s 16s', self.raw_data[:40])
        self.VER, self.TC, self.Qos = get_ver_TC_QOS(ver_TC_QOS)
        try:
            self.NEXTHEAD = IP_PROTOCOL[nexthead]
        except:
            self.NEXTHEAD = nexthead

        self.SRC_IPv6 = get_IP6_addr(src)
        self.DEST_IPv6 = get_IP6_addr(dest)
        self.other_data = self.raw_data[40:]

    def print_result(self):
        print('IP6 --- Destination: {}, Source: {}, NextHead: {}'.format(self.DEST_IPv6, self.SRC_IPv6, self.NEXTHEAD))

    def get_Info(self):
        info = {}
        info['version'] = '[4 bit]' + str(self.VER)
        info['Diff_service'] = '[8 bit]' + str(self.TC)
        info['Qos'] = '[20 bit]' + str(self.Qos)
        info['payload'] = '[16 bit]' + str(self.PAYLOAD_LEN)
        info['IPv6_next_head'] = '[8 bit]' + str(self.NEXTHEAD)
        info['hop_limit'] = '[8 bit]' + str(self.HOPLIMIT)
        info['SRC_IPv6'] = '[128 bit]' + str(self.SRC_IPv6 )
        info['DEST_IPv6'] = '[128 bit]' + str(self.DEST_IPv6)
        return (info, 'IPv6')

    def deal_data(self):
        if self.NEXTHEAD == 'IPv6-ICMP':
            '''互联网控制消息协议'''
            return IPv6_ICMP(self.other_data)
        elif self.NEXTHEAD == 'TCP':
            '''传输控制协议'''
            return TCP(self.other_data)
        elif self.NEXTHEAD == 'UDP':
            '''用户数据报协议'''
            return UDP(self.other_data)
        else:
            ''' 启用了 扩展 头部 '''
            for i in range(40, len(self.raw_data), 20):
                self.other_data = self.raw_data[40+i:]
                nexthead = truct.unpack('! B ', self.raw_data[i:i+20])
                try:
                    NEXTHEAD = IP_PROTOCOL[nexthead]
                except:
                    NEXTHEAD = nexthead
                if NEXTHEAD == 'TCP':
                    return TCP(self.other_data)
                elif NEXTHEAD == 'UDP':
                    return UDP(self.other_data)
                elif NEXTHEAD == 'IPv6-ICMP':
                    return IPv6_ICMP(self.other_data)

                else:
                    print("扩展头部: "+ NEXTHEAD)
            
        
