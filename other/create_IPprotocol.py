import os
import pickle
f = open('ip.html','r')
count = 0
num = 0
low = None
high = None
protocol = {}
for line in f.readlines():
    if not str(line).find('<tr>') == -1:
        count = 0
        continue
    elif not str(line).find('</td>') == -1:
        if count == 0:
            try:
                num = int(str(line)[4:-6], 10)
            except:
                # print(str(line)[4:-6])
                low,high = str(line)[4:-6].split('-')
        elif count == 2:
            if low == None:
                protocol[num] = str(line)[4:-6]
            else:
                for i in range(int(low,10), int(high,10)+1):
                    protocol[i] = str(line)[4:-6]
                low = None
        count += 1
f.close()
# print(protocol)
# pickle.dump(protocol,open("IPprotocol",'wb'))
pic = pickle.load(open("IPprotocol",'rb'))
print(pic)