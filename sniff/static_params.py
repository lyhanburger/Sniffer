'''
in this project, we only pay attention to a part of types
# 0x0800   IP
# 0x0806   ARP
# 0x0808   Frame Relay ARP [RFC1701] 
# 0x6559   Raw Frame Relay [RFC1701] 
# 0x8035   DRARP：Dynamic RARP / RARP：Reverse Address Resolution Protocol
# 0x80F3   AppleTalk（AARP：AppleTalk Address Resolution Protocol）
# 0x8100   以太网自动保护开关（EAPS：Ethernet Automatic Protection Switching）
# 0x8137   因特网包交换（IPX：Internet Packet Exchange）
# 0x814C   简单网络管理协议（SNMP：Simple Network Management Protocol）
# 0x86DD   网际协议v6 （IPv6，Internet Protocol version 6）
# 0x880B   点对点协议（PPP：Point-to-Point Protocol）
# 0x880C   通用交换管理协议（GSMP：General Switch Management Protocol）
# 0x8847   多协议标签交换（单播） MPLS：Multi-Protocol Label Switching <unicast>）
# 0x8848   多协议标签交换（组播）（MPLS, Multi-Protocol Label Switching <multicast>）
# 0x8863   以太网上的 PPP（发现阶段）（PPPoE：PPP Over Ethernet <Discovery Stage>）
# 0x8864   以太网上的 PPP（PPP 会话阶段） （PPPoE，PPP Over Ethernet<PPP Session Stage>）
# 0x88BB   轻量级访问点协议（LWAPP：Light Weight Access Point Protocol）
# 0x88CC   链接层发现协议（LLDP：Link Layer Discovery Protocol）
# 0x8E88   局域网上的 EAP（EAPOL：EAP over LAN）
# 0x9100   VLAN 标签协议标识符（VLAN Tag Protocol Identifier）
# 0x9200   VLAN 标签协议标识符（VLAN Tag Protocol Identifier）
'''
import os
import pickle
# 持久化对象
# f = open('protocol_type') 
# data = f.read()
# data = data.split('\n')
# protocol = {}
# for lines in data:
#     l = lines.split(' ')
#     num = l[0]
#     ty = l[-1]
#     protocol[int(num, 16)] = ty
# f.close()
# f = open("frame_type", "wb")
# pickle.dump(protocol, f)
# f.close()
FRAME_TYPE = pickle.load(open("frame_type", "rb"))
