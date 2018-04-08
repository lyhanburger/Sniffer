import pcap
#  dpkt 测试
# import dpkt

from logcmd import printINFO, printTEST
from extra_Enth import extra_Ethernet

def capt_data(eth_name="en1", p_type=None):

    pc = pcap.pcap(eth_name,timeout_ms=5)
    # pc.setfilter('tcp port 80')  # 设置监听过滤器

    print("capturing")
    for ts, pkt in pc:
        eth = extra_Ethernet(pkt)
        # printINFO("解码1")
        print('Destination: {}, Source: {}, Protocol: {}'.format(eth.dest_mac, eth.src_mac, eth.proto))
        # print("*"*80)
        # en2 = dpkt.ethernet.Ethernet(pkt)
        # printINFO("解码2"+str(en2.data.__class__.__name__) )
        # print(en2.data)
        # print("*"*80)
     
        

# def sniff(offonline = None,store = None):
#   '''
#   offonline : is a .pcap file name, only to read it
#   store : is a .pcap file name, after capture, store them
#     '''

capt_data()
