import struct
from ._static import IP_PROTOCOL

class IP(object):
    def __init__(self, other_data):
        self.rawdata = other_data

    @staticmethod
    def get_protocol(self, num_pro):
        try:
            return IP_PROTOCOL[num_pro]
        except:
            print("ERROR")

    def get_info(self):
        self.ver, self.hlen, self.TOS, self.totalen, self.sign, self.sig, self.offset, self.alive, proco, self.checksum= struct.unpack('H H s 16s 16s 3s 13s 8s 8s 16s', self.raw_data[:20]) # mac des/src :6; type:2
        self.dest_mac = self.get_mac_addr(dest)
        self.src_mac = self.get_mac_addr(src)
        self.ftype = self.get_FrameType(ftype)
        self.other_data = self.raw_data[14:]

        