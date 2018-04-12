from PyQt5.QtCore import *
import pcap
import time
from protocol import handle_Ftype_factory
from common.logcmd import printINFO, printTEST
from common.address import get_raw_data
from ethFrame.extra_Ethernet import extra_Ethernet

# 以太网帧 工厂模式
FrameType = handle_Ftype_factory()

class cap_package(QThread):
    signal_packdict = pyqtSignal(dict)
    def __init__(self, parent = None):
        super(cap_package, self).__init__(parent)
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.sendpackage)
        self.package = []

    def run(self):
        print('caping')
        self.Info = {}
        pc = pcap.pcap(self.eth_name,timeout_ms=1)

        for ts, pkt in pc:
            # INFO__rawData
            self.Info['rawData'] = {}
            self.Info['rawData']['data'] = get_raw_data(pkt)
            self.Info['rawData']['time'] = ts
            

            eth = extra_Ethernet(pkt) 
            printINFO("以太网解码：")
            print('Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.ftype))
            
            # INFO__ethernet
            self.Info['ethernet'] = eth.get_Info()

            ''' dpkt 测试 <课程设计当然不能这么偷懒啦> '''
            import dpkt
            en2 = dpkt.ethernet.Ethernet(pkt)
            try:
                # printTEST(str(en2.data.__class__.__name__)+" "+str(en2.data.data.__class__.__name__))
                printTEST(str(en2.data.data.sport)+"   "+str(en2.data.data.dport))
            except:
                printTEST(str(en2.data.__class__.__name__)+"en2.data.data")

            cur_frame = FrameType.factor_Frame_Type(eth.ftype, eth.other_data)

            if cur_frame:
                curinfo = cur_frame.get_Info()
                self.Info[curinfo[-1]] = curinfo[0]
                printINFO(eth.ftype + " 数据报 数据分析：")
                cur_frame.print_result()


                proto_data = cur_frame.deal_data()

                if not proto_data == None:
                    curinfo = proto_data.get_Info()
                    self.Info[curinfo[-1]] = curinfo[0]
                    proto_data.print_result()
            
            # 控制输出
            time.sleep(1)
            self.signal_packdict.emit(self.Info)
           
        
    def setstuid(self, eth_name = None):
        self.eth_name = eth_name
        self.start()
