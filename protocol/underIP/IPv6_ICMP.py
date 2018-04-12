import struct
from common.static import IPV6_ICMPTYPE


class IPv6_ICMP(object):
    """docstring for IPv6_ICMP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        '''未做 code'''
        ty, self.CODE, self.CHECKSUM, self.INFO = struct.unpack('! B B H I', self.raw_data[:8])
        self.other_data = self.raw_data[8:]
        try:
            self.TYPE = IPV6_ICMPTYPE[ty]
        except:
            self.TYPE = "Unassigned"
       
    def print_result(self):
        print('IPv6_ICMP --- TYPE: {}'.format(self.TYPE))

    def get_Info(self):
        info = {}
        info['ICMPv6_type'] = '[8 bit]' + str(self.TYPE)
        info['ICMPv6_code'] = '[8 bit]' + str(self.CODE)
        info['checksum'] = '[16 bit]' + str(self.CHECKSUM)
        info['info'] = '[32 bit]' + str(self.INFO)
        return(info, 'IPv6_ICMP')
