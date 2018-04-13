import smopy
import urllib.request as urllib2
import sys
from PyQt5.QtCore import *
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
sys.path.append("..")
from common.logcmd import printWARN  

def Get_Average(l):
    sum = 0
    for item in l:
        sum += item
    return sum/len(l)

def get_XY(ip):
    try:
        res = urllib2.urlopen("http://freegeoip.net/json/"+ip)
        a = res.read()
        b = eval(a)
       
        return(b['latitude'], b['longitude'])
    except:
        return None
    
      
def get_img(IP_list_tuple, myIP):

    IP_xy = []

    for IP_tuple in IP_list_tuple:
        for i in IP_tuple:
            if not i == myIP:
                XY = get_XY(ip = i)
                if not XY == None:
                    IP_xy.append(XY)
 
    mp = smopy.Map((min(IP_xy)[0], min(IP_xy)[1], max(IP_xy)[0], max(IP_xy)[1]),z=5)
    x = []
    y = []
    for xy in IP_xy:
        x1, y1 = mp.to_pixels(xy[0], xy[1])
        x.append(x1)
        y.append(y1)
    mp.save_png("curmap.png")
    plt.figure()
    ax = plt.subplot(111)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.xlim(0, mp.w)
    plt.ylim(mp.h, 0)
    plt.axis('off')
    plt.tight_layout()
    ax.imshow(mp.img)
    ax.plot(x, y, 'or', ms=10, mew=2)
    plt.savefig("plot.png")
    

class getIMG(QThread):
    signal_isgetIMG = pyqtSignal()
    def __init__(self, parent = None):
        super(getIMG, self).__init__(parent)
        
    def run(self):
        get_img(self.IPlist, self.myIP)
        self.signal_isgetIMG.emit()
    
    def setIP(self,IP_list_tuple, myIP):
        self.IPlist = IP_list_tuple
        self.myIP = myIP
        self.start()


