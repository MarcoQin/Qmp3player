# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Fri Oct 16 13:06:25 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from threading import Thread
import time
from random import randint

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class t(QtCore.QThread):

    def run(self):
        pass


class Danmu(QtCore.QObject):
    __slots__ = ['label', 'parent', 'anim']

    def __init__(self, label, parent):
        self.label = label
        self.parent = parent


    def move(self):
        self.anim = QtCore.QPropertyAnimation(self.label, 'geometry', self.parent)
        self.anim.setDuration(20*1000)
        #  print self.anim.finished.connect(self.die, QtCore.SLOT('close()'))
        #  print self.anim.stateChanged.connect(self.go)
        self.anim.setStartValue(QtCore.QRect(self.label.pos().x(), self.label.pos().y(), self.label.width(), self.label.height()))
        self.anim.setEndValue(QtCore.QRect(-self.label.width(), self.label.pos().y(), self.label.width(), self.label.height()))
        self.anim.start(QtCore.QPropertyAnimation.DeleteWhenStopped)
        def pp():
            self.die()
            print 'haha'
        self.anim.finished.connect(pp)

    def go(self, t):
        print t

    def die(self):
        print 'haha'
        print self.label
        self.label.deleteLater()


class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.stop = False
        self.setupUi(self)

    def closeEvent(self, *args, **kwargs):
        self.stop = True

    def danmu(self, *labels):
        txt = 'haha'
        i = 1
        while 1:
            i += 1
            if self.stop:
                break
            txt += ' '
            if len(txt) > 300:
                txt = 'test'
            #  for label in labels:
                #  label.setText(txt)
            #  self.label1.setText(txt)
            label = getattr(self, 'label{}'.format(randint(0, 11)))
            print label
            if label:
                label.setText(txt)
            if i > 3:
                if label:
                    label.deleteLater()
                    setattr(self, 'label{}'.format(randint(0, 11)), None)

            time.sleep(1)

    def single_danmu(self, *labels):
        while 1:
            if self.stop:
                break
            for label in labels:
                label.move()
            break
            time.sleep(1)
            #  time.sleep(0.01)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        #  self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        #  self.centralwidget.setStyleSheet('background: black')
        self.label0 = QtGui.QLabel(self.centralwidget)
        self.label0.setGeometry(QtCore.QRect(620, 20, 40, 20))
        self.label0.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label0.setObjectName(_fromUtf8("label"))
        self.label0.setStyleSheet('color: white')
        self.label1 = QtGui.QLabel(self.centralwidget)
        self.label1.setGeometry(QtCore.QRect(620, 40, 40, 20))
        self.label1.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.label1.setStyleSheet('color: white')
        self.label0.setText(_translate("MainWindow", "0", None))
        self.label1.setText(_translate("MainWindow", "1", None))
        print self.label1.mapToGlobal(self.label1.pos())
        print self.label1.pos().x()
        print self.size().width()
        #  self.label1.move(QtCore.QPoint(40, 40))
        labels = []
        for i in range(2):
            setattr(self, 'l%s'%i, QtGui.QLabel(self.centralwidget))
            l = getattr(self, 'l%s'%i)
            l.setGeometry(QtCore.QRect(620, 20*(i+2), 0, 0))
            l.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
            l.setStyleSheet('color: white')
            des = QtGui.QGraphicsDropShadowEffect()
            des.setOffset(0,0)
            des.setBlurRadius(6)
            des.setColor(QtGui.QColor('black'))
            l.setGraphicsEffect(des)
            txt = 'test danmaku %s'%i
            l.setText(txt)
            fm = l.fontMetrics()
            print fm.width(txt)
            print fm.height()
            l.setFixedWidth(fm.width(txt))
            l.setFixedHeight(fm.height())
            l.font().setBold(True)
            l.font().setPointSize(24)
            labels.append(Danmu(l, self))
        labels.append(Danmu(self.label0, self))
        labels.append(Danmu(self.label1, self))

        for item in labels:
            item.move()
        #  Thread(target=self.single_danmu, args=labels).start()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        #  Thread(target=self.danmu, args=(self.label0, self.label1)).start()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    gui = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.show()
    sys.exit(app.exec_())
