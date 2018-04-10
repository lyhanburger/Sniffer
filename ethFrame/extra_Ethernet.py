import struct
from .static import FRAME_TYPE

class extra_Ethernet:
    def __init__(self,data):
        self.raw_data = data
        self.get_des_src_type()

    @staticmethod
    def get_FrameType(prototype):
        try:
            return FRAME_TYPE[prototype]
        except:
            return "Others"
        
    def get_des_src_type(self):
        dest, src, ftype = struct.unpack('! 6s 6s H', self.raw_data[:14]) # mac des/src :6; type:2
        self.dest_mac = self.get_mac_addr(dest)
        self.src_mac = self.get_mac_addr(src)
        self.ftype = self.get_FrameType(ftype)
        self.other_data = self.raw_data[14:]
    
    # Returns MAC as string from bytes (ie AA:BB:CC:DD:EE:FF)
    def get_mac_addr(self,mac_raw):
        byte_str = map('{:02x}'.format, mac_raw)
        mac_addr = ':'.join(byte_str).upper()
        return mac_addr



