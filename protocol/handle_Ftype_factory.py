from .handle_IP import IP
class handle_Ftype_factory(object):
    """docstring for handle_Type_factory"""
    def __init__(self):
        pass

    def factor_Frame_Type(self,ftype,other_data):
        if ftype == "IP":
            return IP(other_data)
        elif ftype == "ARP":
            pass
        elif ftype == "IPv6":
            pass
        elif ftype == "PPP":
            pass
        elif ftype == "LLDP":
            pass
        else:
            # 只识别不做分析
            pass
