import struct

class ARP(object):
    """docstring for ARP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        self.SHA, procotol, self.LEN_MAC, self.LEN_IP, self.TYPE, self.SRC_MAC, self.SRC_IP, self.DEST_MAC, self.DEST_IP = struct.unpack('H H B B H 6s 4s 6s 4s', self.raw_data[:28])

    def print_result(self):
        print('Destination: {}, Source: {}, Protocol: {}'.format(self.DEST_IP4, self.SRC_IP4, self.PROTOCOL))
