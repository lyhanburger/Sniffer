import struct
import sys
sys.path.append("..")
from common.static import FRAME_TYPE
from common.address import get_mac_addr
from common.logcmd import printWARN

class extra_Ethernet:
    def __init__(self,data):
        self.raw_data = data
        self.get_des_src_type()

    @staticmethod
    def get_FrameType(prototype):
        try:
            return FRAME_TYPE[prototype]
        except:
            printWARN("extra_Ethernet<get_FrameType> not find "+prototype)
            return str(prototype)

        
    def get_des_src_type(self):
        dest, src, ftype = struct.unpack('! 6s 6s H', self.raw_data[:14]) # mac des/src :6; type:2
        self.dest_mac = get_mac_addr(dest)
        self.src_mac = get_mac_addr(src)
        self.ftype = self.get_FrameType(ftype)
        self.other_data = self.raw_data[14:]

    def get_Info(self):
        info = {}
        info['eth_dest_mac'] = '[48 bit]' + self.dest_mac
        info['eth_src_mac'] = '[48 bit]' + self.src_mac
        info['frame_type'] = '[16 bit]' + self.ftype
        return info


    
   



