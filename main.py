import pcap
from protocol import handle_Ftype_factory
from common.logcmd import printINFO, printTEST
from ethFrame.extra_Ethernet import extra_Ethernet

# 以太网帧 工厂模式
FrameType = handle_Ftype_factory()

def capt_data(eth_name="en1", p_type=None):

    pc = pcap.pcap(eth_name,timeout_ms=3)
    # pc.setfilter('ip')  # 设置监听过滤器

    print("capturing")
    for ts, pkt in pc:

        eth = extra_Ethernet(pkt)

        printINFO("以太网解码：")
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.ftype))

        # dpkt 测试
        import dpkt
        en2 = dpkt.ethernet.Ethernet(pkt)
        printTEST(str(en2.data.__class__.__name__)+" "+str(en2.data.data.__class__.__name__))

        if eth.ftype == 'IP':
            cur_frame = FrameType.factor_Frame_Type(eth.ftype, eth.other_data)
            printINFO(eth.ftype + " 数据报 数据分析：")
            cur_frame.print_result()
        
            proto_data = cur_frame.deal_data()
            if not proto_data == None:
                proto_data.print_result()
            
       
        # print(en2.data)
        # print("*"*80)
          
# def sniff(offonline = None,store = None):
#   '''
#   offonline : is a .pcap file name, only to read it
#   store : is a .pcap file name, after capture, store them
#     '''
capt_data()