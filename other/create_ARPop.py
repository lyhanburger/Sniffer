import os
import pickle
info = {}
# f = open("arp-parameters-1.csv",'r')
f = open("arp-parameters-2.csv",'r')
i =0 
for line in f.readlines():
    if i == 0:
        i+= 1
        continue
    l = line.split(',')
    try:
        info[int(l[0],10)] = l[1]
    except:
        pass
print(info)
f.close()
# pickle.dump(info,open('arp_op','wb'))
pickle.dump(info,open('arp_hardware','wb'))
# print(pickle.load(open('arp_op','rb')))
# print(pickle.load(open('arp_hardware','rb')))