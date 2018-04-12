from PyQt5.QtCore import *
import pcap
from protocol import handle_Ftype_factory
from common.logcmd import printINFO, printTEST
from ethFrame.extra_Ethernet import extra_Ethernet

# 以太网帧 工厂模式
FrameType = handle_Ftype_factory()

class cap_package(QThread):
    signal_packlist = pyqtSignal(list)
    def __init__(self, parent = None):
        super(cap_package, self).__init__(parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sendpackage)
        self.package = []

    def run(self):
        Info = {}
        pc = pcap.pcap(self.eth_name,timeout_ms=1)

        for ts, pkt in pc:
            Info['rawData'] = pkt
            eth = extra_Ethernet(pkt) 
            printINFO("以太网解码：")
            print('Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.ftype))
            # dpkt 测试
            import dpkt
            en2 = dpkt.ethernet.Ethernet(pkt)
            try:
                # printTEST(str(en2.data.__class__.__name__)+" "+str(en2.data.data.__class__.__name__))
                printTEST(str(en2.data.data.sport)+"   "+str(en2.data.data.dport))
            except:
                printTEST(str(en2.data.__class__.__name__)+"en2.data.data")

            cur_frame = FrameType.factor_Frame_Type(eth.ftype, eth.other_data)
            if cur_frame:
                printINFO(eth.ftype + " 数据报 数据分析：")
                cur_frame.print_result()
                proto_data = cur_frame.deal_data()
                if not proto_data == None:
                    proto_data.print_result()

                self.package = capt_data(eth_name = self.eth_name)
                self.timer.start(1000) #ms
            
    def sendpackage(self):
        self.signal_list.emit(self.package)

    def setstuid(self, eth_name = None):
        self.eth_name = eth_name
        self.start()
