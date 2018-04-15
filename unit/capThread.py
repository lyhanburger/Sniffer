from PyQt5.QtCore import *
import pcap
import time
from protocol import handle_Ftype_factory
from common.logcmd import printINFO, printTEST, printWARN
from common.address import get_raw_data
from ethFrame.extra_Ethernet import extra_Ethernet
import socket
# 以太网帧 工厂模式
FrameType = handle_Ftype_factory()

class cap_package(QThread):
    signal_packdict = pyqtSignal(dict)
    signal_iptuple = pyqtSignal(tuple)
    signal_portstr = pyqtSignal(str)
    def __init__(self, parent = None):
        super(cap_package, self).__init__(parent)
        self.package = []
        self.is_stop = False
        self.myIP = socket.gethostbyname(socket.gethostname())
        

    def stop(self):
        printWARN("STOP Thred")
        self.is_stop = True

    def restart(self):
        printWARN("START Thred")
        self.is_stop = False

    def change_status(self, cur):
        self.status = cur

    def run(self):
        print('caping')
        Info = {}
        src_dest_ip = None
        port = None
        pc = pcap.pcap(self.eth_name,timeout_ms=1)

        for ts, pkt in pc:
            # INFO__rawData
            Info['rawData'] = {}
            Info['rawData']['data'] = get_raw_data(pkt)
            Info['rawData']['time'] = ts
            eth = extra_Ethernet(pkt) 
            printINFO("以太网解码：")
            print('Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.ftype))
            
            # INFO__ethernet
            Info['ethernet'] = eth.get_Info()

            ''' dpkt 测试 <课程设计当然不能这么偷懒啦> '''
            # import dpkt
            # en2 = dpkt.ethernet.Ethernet(pkt)
            # try:
            #     # printTEST(str(en2.data.__class__.__name__)+" "+str(en2.data.data.__class__.__name__))
            #     printTEST(str(en2.data.data.sport)+"   "+str(en2.data.data.dport))
            # except:
            #     printTEST(str(en2.data.__class__.__name__)+"en2.data.data")

            cur_frame = FrameType.factor_Frame_Type(eth.ftype, eth.other_data)

            if cur_frame:
                curinfo = cur_frame.get_Info()
                Info[curinfo[-1]] = curinfo[0]
                src_dest_ip = cur_frame.get_IP()

                printINFO(eth.ftype + " 数据报 数据分析：")
                cur_frame.print_result()

                proto_data = cur_frame.deal_data()

                if not proto_data == None:
                    curinfo = proto_data.get_Info()
                    if not src_dest_ip == None and (curinfo[-1] == "TCP" or curinfo[-1] == "UDP"):
                        if self.myIP in src_dest_ip:
                            port = ""
                    Info[curinfo[-1]] = curinfo[0]
                    proto_data.print_result()
            
            # 控制输出
            if self.status == 0:
                '''cap'''
                if not port == None :
                    self.signal_portstr.emit(port)
                if not src_dest_ip == None :
                    self.signal_iptuple.emit(src_dest_ip)
                self.signal_packdict.emit(Info)
                time.sleep(1)
            elif self.status == 1:
                '''flow'''
                if not src_dest_ip == None :
                    self.signal_iptuple.emit(src_dest_ip)
                if not port == None :
                    self.signal_portstr.emit(port)
                self.signal_packdict.emit(Info)
            else:
                if self.is_stop:
                    break
                if not port == None :
                    self.signal_portstr.emit(port)
                    
                self.signal_packdict.emit(Info)
                if src_dest_ip == None:
                    continue
                self.signal_iptuple.emit(src_dest_ip)
              
           
        
    def setstuid(self, eth_name = None):
        self.eth_name = eth_name
    
