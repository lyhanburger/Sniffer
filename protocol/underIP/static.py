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