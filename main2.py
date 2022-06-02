import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication,QPropertyAnimation,QDate,QDateTime,
                            QMetaObject,QObject,QPoint,QRect,QSize,QTime,QUrl,Qt,QEvent)
from PySide2.QtGui import (QBrush,QColor,QConicalGradient,QCursor,QFont,QFontDatabase,QIcon,QKeySequence,QLinearGradient
,QPalette,QPainter,QPixmap,QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication,QComboBox,QPushButton,QVBoxLayout,QWidget
from PyQt5.QtCore import Qt

from ui_main_1 import Ui_MainWindow

from ui_functions import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        def moveWindow(event):

            if UIFunctions.returnStatus() == 1:
                UIFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.title_bar.mouseMoveEvent = moveWindow

        UIFunctions.uiDefinitions(self)



        self.show()

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
