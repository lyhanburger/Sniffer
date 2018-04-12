'''互联网控制消息协议'''
import sys
sys.path.append("...")
from common.static import ICMPTYPE
from common.logcmd import printWARN

import struct

class ICMP(object):
    """docstring for ICMP"""
    def __init__(self, data):
        self.raw_data = data
        self.analysis()

    def analysis(self):
        '''Echo Reply : return ID, sequence'''
        itype, code, self.CHECKSUM, self.ID, self.SEQUEN = struct.unpack('! B B H H H', self.raw_data[:8])
        self.TYPEINFO = self.get_type(itype, code)
        self.other_data = self.raw_data[8:]

    def get_type(self, itype, code):
        try:
            code_key = list(ICMPTYPE[str(itype)].keys())
            if code_key[0] == 'x':
                ''' random code '''
                return ICMPTYPE[str(itype)]['x']
            elif len(code_key) == 1 and code_key[0] == '0':
                return ICMPTYPE[str(itype)]['0']
            else:
               return ICMPTYPE[str(itype)][str(code)]
        except:
            printWARN('icmp key ERROR ', str(itype) , str(code))
            return None

    def print_result(self):
        if self.TYPEINFO  == None:
            printWARN("ERROR")
        else:
            print('type: {}'.format(self.TYPEINFO.replace("_"," ")) )

    def get_Info(self):
        info = {}
        info['ICMP_type'] = '[16 bit]' + str(self.TYPEINFO)
        info['checksum'] = '[16 bit]' + str(self.CHECKSUM)
        info['ID'] = '[16 bit]' + str(self.ID)
        info['sequence'] = '[16 bit]' + str(self.SEQUEN)
        return(info, 'ICMP')



