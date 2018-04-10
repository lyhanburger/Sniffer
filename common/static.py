import pickle
import os

'''
ICMPTYPE = {
    'type(str)':{
        'code(str)': 'description(str)''
    }
}
'''
ICMPTYPE = pickle.load(open('_static/icmpType','rb'))

'''
IP_PROTOCOL={
    i(int): 'protocol(str)'
}
'''
IP_PROTOCOL = pickle.load(open("_static/IPprotocol",'rb'))

'''
FRAME_TYPE={
    i(int): 'frame_type(str)'
}
'''
FRAME_TYPE = pickle.load(open("_static/FrameType", "rb"))
