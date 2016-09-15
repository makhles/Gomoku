from PyQt4 import QtGui, QtCore
import os

class Square(QtGui.QLabel):

    def __init__(self, parent, m, n):
        QtGui.QLabel.__init__(self, parent)
        self.name = 'Square[' + str(m) + '][' + str(n) + ']'
        self.m = m
        self.n = n

    def __repr__(self):
        return self.name

    def mouseReleaseEvent(self, ev):
        self.emit(QtCore.SIGNAL('clicked()'))

    def getCoord(self):
        return self.m, self.n

    def setNormal(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/lightTile.png"))

    def setNormal2(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/darkTile.png"))

    def setBlackStone(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/blackStone.png"))

    def setWhiteStone(self):
        self.setPixmap(QtGui.QPixmap(os.getcwd() + "/img/whiteStone.png"))
