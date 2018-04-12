from Ui_window import *
from capThread import cap_package
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
class WINGUI(QMainWindow):
    """docstring for window"""
    # cap_package_signal = pyqtSignal(list) 
    def __init__(self,parent=None):
        super(WINGUI, self).__init__(parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)

        ##########package########
        self.list_package = []

        ##########线程#########
        self.Thread_cap = cap_package()
        self.Thread_cap.signal_packdict .connect(self.get_package)

        ##########table##########
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True);
        self.ui.tableWidget.setHorizontalHeaderLabels(['time','package'])
        self.ui.tableWidget.verticalHeader().setDefaultSectionSize(15)
        self.ui.tableWidget.setAlternatingRowColors(True);
        self.ui.tableWidget.verticalHeader().setHidden(True);

        ##########tree###########
        self.ui.treeWidget.setHeaderLabel("当前协议")


    ############# UI SLOT ################
    def isLineEditEmpty(self):
        if self.ui.lineEdit.text() == '':
            self.ui.pbt.setEnabled(False)
        else:
            self.ui.pbt.setEnabled(True)

    def capt(self):
        '''capture package'''
        name = self.ui.lineEdit.text()
        print('web device:',name)
        self.Thread_cap.setstuid(eth_name = name)
        self.Thread_cap.start()
        self.ui.statusbar.showMessage("大王，小的抓包去了(=ﾟωﾟ)ﾉ", 3000);
    
    def showPage(self, btn_id):
        self.ui.stackedWidget.setCurrentIndex(btn_id)

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
                    curTrans = ccurTrans[curTrans.find(']')+1:]
                else:
                    QTreeWidgetItem(frame_type, [key+" : "+self.list_package[row][curtype][key]])
            for key in self.list_package[row][curTrans]:
                QTreeWidgetItem(IP_type, [key+" : "+self.list_package[row][curtype][key]])
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
        
       

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = WINGUI()
    win.show()
    sys.exit(app.exec_())
