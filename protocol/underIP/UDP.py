import struct

class UDP(object):
    """docstring for UDP"""
    def __init__(self, arg):
        self.raw_data = arg
        self.__analysis()
        
    def __analysis(self):
        '''Port number to identify sending and receiving application end-points on a host'''
        self.SRC_PORT, self.DEST_PORT, self.LEN, self.CHECKSUM,  = struct.unpack('H H H H', self.raw_data[:8])
        self.other_data = self.raw_data[8:]
       

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

    def print_result(self):
        print('UDP --- SRC_PORT: {}, DEST_PORT: {}'.format(self.SRC_PORT, self.DEST_PORT))
