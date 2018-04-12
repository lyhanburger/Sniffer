import struct

class UDP(object):
    """docstring for UDP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()

    def __analysis(self):
        '''Port number to identify sending and receiving application end-points on a host'''
        self.SRC_PORT, self.DEST_PORT, self.LEN, self.CHECKSUM,  = struct.unpack('! H H H H', self.raw_data[:8])
        self.other_data = self.raw_data[8:]
       
    def print_result(self):
        print('UDP --- SRC_PORT: {}, DEST_PORT: {}'.format(self.SRC_PORT, self.DEST_PORT))

    def get_Info(self):
        info = {}
        info['SRC_PORT'] = '[16 bit]' + str(self.SRC_PORT)
        info['DEST_PORT'] = '[16 bit]' + str(self.DEST_PORT)
        info['length'] = '[16 bit]' + str(self.LEN)
        info['checksum'] = '[16 bit]' + str(self.CHECKSUM)
        return(info, 'UDP')

    def up_layer(self, PORT):
        if PORT == 20 or PORT == 21:
            '''FTP'''
            pass
        elif PORT == 23:
            '''TELNET '''
            pass
        elif PORT == 25:
            '''SMTP'''
            pass
        elif PORT == 443:
            '''HTTP over SSL/TLS '''
            pass
        elif PORT == 80:
            ''' HTTP '''
            pass
        else:
            '''Other up procotol'''
            pass

    
