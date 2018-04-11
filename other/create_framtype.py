import os
import pickle
# # 持久化对象
# info = {}
# f = open('ieee-802-numbers-1.csv','r') 
# for line in f.readlines():
#     l = line.split(',')
#     try:
#         info[int(l[0],16)] = l[1]
#     except:
#         low,high = l[0].split('-')
#         low = int(low, 16)
#         high = int(high, 16)
#         for i in range(low, high+1):
#             info[i] = l[1]
# f.close()

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
# pickle.dump(info, f)
# f.close()

print(pickle.load(open("frame_type", "rb")))