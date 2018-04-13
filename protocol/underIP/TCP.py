import struct
import re
import sys
sys.path.append("...")
from common.logcmd import printINFO, printWARN

define_FLAGS={0:'URG',1:'ACK',2:'PSH', 3:'RST', 4:'SYN', 5:'FIN'}

class TCP(object):
    """docstring for TCP"""
    def __init__(self, data):
        self.raw_data = data
        self.__analysis()

    def __analysis(self):
        '''Port number to identify sending and receiving application end-points on a host'''
        self.SRC_PORT, self.DEST_PORT, self.SEQ, self.ACK, THL_R_FLAG, self.WIN_SIZE, self.CHECKSUM, self.URGENR_PTR = struct.unpack('! H H I I H H H H', self.raw_data[:20])
        self.THL, self.R, self.FLAG = self.__get_THL_R_FLAG(THL_R_FLAG)
        if self.THL > 5:
            self.OPTION = self.raw_data[20:24]
            self.other_data = self.raw_data[24:]
        else:
            self.OPTION = None
            self.other_data = self.raw_data[20:]

    def print_result(self):
        print('TCP --- SRC_PORT: {}, DEST_PORT: {}'.format(self.SRC_PORT, self.DEST_PORT))
        
    def __get_THL_R_FLAG(self, THL_R_FLAG):
        THL = THL_R_FLAG >> 12
        R = THL_R_FLAG >> 6 & 0x003F
        FLAG = THL_R_FLAG & 0x003F
        FLAG = '{:b}'.format(FLAG)
        return (THL, R, FLAG)

    def get_FLAGS(self):
        '''
        Eg. 
        return ['ACK', 'PSH'...]

        '''
        numl = list( m.start() for m in re.finditer('1', self.FLAG))
        flag = []
        for item in numl:
            flag.append(define_FLAGS[item])
        return flag 

    def get_Info(self):
        info = {}
        info['SRC_PORT'] = '[16 bit]' + str(self.SRC_PORT)
        info['DEST_PORT'] = '[16 bit]' + str(self.DEST_PORT)
        info['SEQ'] = '[32 bit]' + str(self.SEQ)
        info['ACK'] = '[32 bit]' + str(self.ACK)
        info['TCP_head_length'] = '[4 bit]' + str(self.THL)
        info['reserve'] = '[6 bit]' + str(self.R)
        info['FLAG'] = '[6 bit]' + str(self.FLAG)
        info['window_size'] = '[16 bit]' +str(self.WIN_SIZE)
        info['checksum'] = '[16 bit]' +str(self.CHECKSUM)
        info['urgent_point'] = '[16 bit]' + str(self.URGENR_PTR)
        info['option'] = '[16 bit]' +str(self.OPTION)
        return(info, 'TCP')

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

    