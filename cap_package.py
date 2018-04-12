import pcap
from protocol import handle_Ftype_factory
from common.logcmd import printINFO, printTEST
from ethFrame.extra_Ethernet import extra_Ethernet

# 以太网帧 工厂模式
FrameType = handle_Ftype_factory()

def capt_data(eth_name="en0", p_type=None):
    '''
    pcap(name=None, snaplen=65535, promisc=True, immediate=False, timeout_ms=None) -> packet capture object。Open a handle to a packet capture descriptor.
 
    name      -- name of a network interface or dumpfile to open,
                   or None to open the first available up interface
    snaplen   -- maximum number of bytes to capture for each packet
    promisc   -- boolean to specify promiscuous mode sniffing
    immediate -- disable buffering, if possible
    timeout_ms -- requests for the next packet will return None if the timeout
                        (in milliseconds) is reached and no packets were received
                      (Default: no timeout)
    '''
    pc = pcap.pcap(eth_name,timeout_ms=1)
    print("capturing")
    for ts, pkt in pc:
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


capt_data()       
        
