import os
import pickle
# info = {}
# with open('ICMPTYPE','r') as f:
#     for line in f.readlines():
#         # print(line)
#         ty, code, mm = line.split(' ')
#         if not ty in info.keys():
#             info[ty] = {}
        
#         info[ty][code] = mm.replace('\n','')
# for i in range(42, 253):
#     if not str(i) in info.keys():
#         info[str(i)] = {}
#     info[str(i)]['x'] = 'Reserved'
# for i in range(20, 30):
#     if not str(i) in info.keys():
#         info[str(i)] = {}
#     info[str(i)]['x'] = 'Reserved_for_robustness_experiment'
# f = open('icmpType','wb')
# pickle.dump(info, f)
# f.close()
f = open('icmpType','rb')
ICMPTYPE = pickle.load(f)
f.close()
print(ICMPTYPE['8']['0'])
