import os
import pickle
# # 持久化对象
f = open('protocol_type') 
data = f.read()
data = data.split('\n')
protocol = {}
for lines in data:
    l = lines.split(' ')
    num = l[0]
    ty = l[-1]
    protocol[int(num, 16)] = ty
f.close()
f = open("frame_type", "wb")
pickle.dump(protocol, f)
f.close()