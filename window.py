from unit.Ui_window import *
from unit.capThread import cap_package
from unit.geo import getIMG
from PyQt5 import QtCore, QtGui, QtWidgets
from common.logcmd import printWARN , printTEST
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *
import socket
import time

class WINGUI(QMainWindow):
    """docstring for window"""
    # cap_package_signal = pyqtSignal(list) 
    def __init__(self,parent=None):
        super(WINGUI, self).__init__(parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.set_Png = True
        self.port = 0

        ##########package########
        self.list_package = []
        self.IP_list_tuple = []
        self.myIP = socket.gethostbyname(socket.gethostname())

        ##########线程#########
        self.Thread_cap = cap_package()
        self.Thread_cap.signal_packdict.connect(self.get_package)
        self.Thread_cap.signal_iptuple.connect(self.show_IP)

        self.Image = getIMG()
        self.Image.signal_isgetIMG.connect(self.show_png)
        self.Thread_cap.signal_portstr.connect(self.show_flow)

        ##########table##########
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True);
        self.ui.tableWidget.setHorizontalHeaderLabels(['time','package'])
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(15)
        self.ui.tableWidget.setAlternatingRowColors(True);
        self.ui.tableWidget.verticalHeader().setHidden(True);

        ##########tree###########
        self.ui.treeWidget.setHeaderLabel("当前协议")

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.show_time)

        self.m_chart = QChart();  
        self.chartView = QChartView(self.m_chart);  
        self.chartView.setRubberBand(QChartView.RectangleRubberBand);  

        self.m_series = QLineSeries()  
        self.m_chart.addSeries(self.m_series);  
      
        for i in range(10):  
           self.m_series.append(i,0)  
        
        self.m_series.setUseOpenGL(True)
      
        self.axisX = QValueAxis()
        self.axisX.setRange(0,10);  
        self.axisX.setLabelFormat("%g")  
        self.axisX.setTitleText("axisX")  
      
        self.axisY = QValueAxis()
        self.axisY.setRange(0,1000)
        self.axisX.setLabelFormat("%g") 
        self.axisY.setTitleText("axisY"); 
      
        self.m_chart.setAxisX(self.axisX, self.m_series)  
        self.m_chart.setAxisY(self.axisY, self.m_series)  
        self.m_chart.legend().hide();  
        self.m_chart.setTitle("流量监控");  
        
        self.ui.verticalLayout1.addWidget(self.chartView);

        self.timer.start(800)  
     


    ############# UI SLOT ################
    def isLineEditEmpty(self):
        if self.ui.lineEdit.text() == '':
            self.ui.pbt.setEnabled(False)
        else:
            self.ui.pbt.setEnabled(True)

    def capt(self):
        '''capture package'''
        while self.ui.tableWidget.rowCount()>0:
            self.ui.tableWidget.removeRow(0)
        name = self.ui.lineEdit.text()
        print('device:',name)
        self.list_package.clear()
        self.Thread_cap.setstuid(eth_name = name)
        self.Thread_cap.change_status(0)
        time.sleep(0.5)
        self.Thread_cap.start()
        self.ui.statusbar.showMessage("大王，小的抓包去了(=ﾟωﾟ)ﾉ", 3000);
    
    def showPage(self, btn_id):
        self.ui.stackedWidget.setCurrentIndex(btn_id)
        try:
            self.Thread_cap.change_status(btn_id)
            self.ui.treeWidget.clear()
            # while self.ui.tableWidget.rowCount()>0:
            #     self.ui.tableWidget.removeRow(0)
            self.ui.pbt.setEnabled(False)
            self.ui.lineEdit.clear()
            # self.list_package.clear()
        except:
            pass

    def treeShow(self, Item):
        self.ui.treeWidget.clear()
        row = self.ui.tableWidget.row(Item)
        try:
            eth = QTreeWidgetItem(self.ui.treeWidget, ['ethernet']);
            for key in self.list_package[row]['ethernet']:
                if key == 'frame_type':
                    curtype =  self.list_package[row]['ethernet'][key]
                    frame_type = QTreeWidgetItem(eth, [key+" : "+ curtype])
                    curtype = curtype[curtype.find(']')+1:]
                else:
                    QTreeWidgetItem(eth, [key+" : "+self.list_package[row]['ethernet'][key]])
            for key in self.list_package[row][curtype]:
                if key == 'IPv4_protocol' or key == 'IPv6_next_head':
                    curTrans = self.list_package[row][curtype][key]
                    IP_type = QTreeWidgetItem(frame_type, [key+" : "+ curTrans])
                    curTrans = curTrans[curTrans.find(']')+1:]
                else:
                    QTreeWidgetItem(frame_type, [key+" : "+self.list_package[row][curtype][key]])
            for key in self.list_package[row][curTrans]:
                QTreeWidgetItem(IP_type, [key+" : "+self.list_package[row][curTrans][key]])
        except:
            pass
        # self.list_package[row]['ethernet']

    ############ thread slot #############
    def get_package(self, package_dict):
        self.list_package.append(package_dict)
        self.ui.statusbar.showMessage("大王～包抓来了\(≧▽≦)/", 1500);
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.insertRow(row_count)
        self.ui.tableWidget.setItem(row_count, 0, QTableWidgetItem(str(package_dict['rawData']['time'])))
        self.ui.tableWidget.setItem(row_count, 1, QTableWidgetItem(package_dict['rawData']['data']))
        
    def show_IP(self, IP_tuple):
        
        if str(self.myIP) in IP_tuple:
            self.IP_list_tuple.append(IP_tuple)
            printWARN("IP_tuple"+str(len(self.IP_list_tuple)))
            if len(self.IP_list_tuple) >= 100 and self.set_Png:
                self.set_Png == False  
                # self.Thread_cap.stop()
                self.Image.setIP(self.IP_list_tuple[:100], self.myIP)

    def show_png(self):
        self.set_Png = True
        pix = QPixmap("plot.png")
        pix = pix.scaled(QSize(341, 461), Qt.KeepAspectRatio)
        self.ui.map_label.setPixmap(pix)
        for i in range(100):
            self.IP_list_tuple.pop(0)

    def show_flow(self,port):
        self.port += 1

    def show_time(self):
        # dataTime = QTime(QTime.currentTime())
        # eltime = dataTime.elapsed()
        # lastpointtime = 0
        # size = eltime - lastpointtime
        size = 1
        # printWARN(str(self.port))
        oldPoints = self.m_series.pointsVector()
        points = []
        for i in range(1,len(oldPoints)): 
            points.append(QPointF(i-size ,oldPoints[i].y()))
        sizePoints = len(points)
        for k in range(size): 
            points.append(QPointF(k+sizePoints, self.port));  
        self.m_series.replace(points) 
        self.port = 0
        self.timer.start(800)


        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = WINGUI()
    win.show()
    sys.exit(app.exec_())
