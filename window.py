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
        ##########线程#########
        self.Thread_cap = cap_package()
        self.Thread_cap.signal_packlist.connect(self.get_package)

    ############# UI SLOT ################
    def isLineEditEmpty(self):
        if self.ui.lineEdit.text() == '':
            self.ui.pbt.setEnabled(False)
        else:
            self.ui.pbt.setEnabled(True)

    def capt(self):
        '''capture package'''
        pass
    
    def showPage(self, btn_id):
        self.ui.stackedWidget.setCurrentIndex(btn_id)

    ############ thread slot #############
    def get_package(self, package_list):
        pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    win = WINGUI()
    win.show()
    sys.exit(app.exec_())
