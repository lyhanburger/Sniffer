from .handle_IP import IP
from .handle_ARP import ARP
from .handle_IPv6 import IPv6
class handle_Ftype_factory(object):
    """docstring for handle_Type_factory"""
    def __init__(self):
        pass

    def factor_Frame_Type(self,ftype,other_data):
        if ftype == "IP":
            return IP(other_data)
        elif ftype == "ARP":
            return ARP(other_data)
        elif ftype == "IPv6":
            return IPv6(other_data)
        # elif ftype == "PPP":
        #     pass
        # elif ftype == "LLDP":
        #     pass
        else:
            # 只识别不做分析
            pass
