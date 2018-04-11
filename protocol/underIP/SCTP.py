import struct

class SCTP(object):
    """docstring for SCTP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        ''''''
        self.SRC_PORT, self.DEST_PORT, self.VERTIFY_TAG, self.CHECKSUM = struct.unpack('H H I I', self.raw_data[:6])
        self.other_data = self.raw_data[6:]
       
    def print_result(self):
        print('SCTP --- SRC_PORT: {}, DEST_PORT: {}'.format(self.SRC_PORT, self.DEST_PORT))
        
