# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Whatsapp_Scrapper.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(505, 467)
        self.GroupLabel = QtWidgets.QLabel(Frame)
        self.GroupLabel.setGeometry(QtCore.QRect(140, 140, 91, 31))
        self.GroupLabel.setObjectName("GroupLabel")
        self.startButton = QtWidgets.QPushButton(Frame)
        self.startButton.setGeometry(QtCore.QRect(140, 280, 93, 28))
        self.startButton.setObjectName("startButton")
        self.stopButton = QtWidgets.QPushButton(Frame)
        self.stopButton.setGeometry(QtCore.QRect(260, 280, 93, 28))
        self.stopButton.setObjectName("stopButton")
        self.GroupInput = QtWidgets.QLineEdit(Frame)
        self.GroupInput.setGeometry(QtCore.QRect(240, 150, 113, 22))
        self.GroupInput.setObjectName("GroupInput")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.GroupLabel.setText(_translate("Frame", "Group Name"))
        self.startButton.setText(_translate("Frame", "Start"))
        self.stopButton.setText(_translate("Frame", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())