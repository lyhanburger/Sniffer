import sys
import struct
sys.path.append("...")
from common.static import FRAME_TYPE, ARP_OP, ARP_HARDWARE
from common.logcmd import printWARN
from common.address import get_mac_addr, get_IP4_addr

class ARP(object):
    """docstring for ARP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        SHA, procotol, self.LEN_MAC, self.LEN_IP, OPT, SRC_MAC, SRC_IP, DEST_MAC, DEST_IP = struct.unpack('! H H B B H 6s 4s 6s 4s', self.raw_data[:28])
        self.SRC_MAC = get_mac_addr(SRC_MAC)
        self.SRC_IP = get_IP4_addr(SRC_IP)
        self.DEST_MAC = get_mac_addr(DEST_MAC)
        self.DEST_IP = get_IP4_addr(DEST_IP)
        try:
            self.SHA = ARP_HARDWARE[SHA]
        except:
            self.SHA = 'Unassigned'
        try:
            self.OPT = ARP_OP[OPT]
        except:
            self.OPT = 'Unassigned'
        try:
            self.PROCOTOL = FRAME_TYPE[procotol]
        except:
            self.PROCOTOL = procotol
            printWARN(str(procotol) + " " + "undefined procotol")

    def print_result(self):
        print('OPT: {}, SRC_MAC: {}, SRC_IP: {}, DEST_MAC: {}, DEST_IP: {}'.format(self.OPT, self.SRC_MAC, self.SRC_IP, self.DEST_MAC, self.DEST_IP))
    def deal_data(self):
        return None
        


