import struct
from common.static import IPV6_ICMPTYPE
from common.logcmd import printWARN

class IPv6_ICMP(object):
    """docstring for IPv6_ICMP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        '''未做 code'''
        ty, self.CODE, self.CHECKSUM, self.INFO = struct.unpack('B B H I', self.raw_data[:8])
        self.other_data = self.raw_data[6:]
        try:
            self.TYPE = IPV6_ICMPTYPE[ty]
        except:
            self.TYPE = "Unassigned"
       
    def print_result(self):
        print('IPv6_ICMP --- TYPE: {}'.format(self.TYPE))
