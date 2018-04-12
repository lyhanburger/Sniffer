import struct

class SCTP(object):
    """docstring for SCTP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        ''''''
        self.SRC_PORT, self.DEST_PORT, self.VERTIFY_TAG, self.CHECKSUM = struct.unpack('! H H I I', self.raw_data[:12])
        self.other_data = self.raw_data[6:]
       
    def print_result(self):
        print('SCTP --- SRC_PORT: {}, DEST_PORT: {}'.format(self.SRC_PORT, self.DEST_PORT))

    def get_Info(self):
        info = {}
        info['SRC_PORT'] = '[16 bit]' + str(self.SRC_PORT)
        info['DEST_PORT'] = '[16 bit]' + str(self.DEST_PORT)
        info['vertification_tag'] = '[32 bit]' + str(self.VERTIFY_TAG)
        info['checksum'] = '[32 bit]' + str(self.CHECKSUM)
        return(info, 'SCTP')

