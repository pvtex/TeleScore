# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\component\basiccomp\clockcomp.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(110, 80)
        Form.setMinimumSize(QtCore.QSize(20, 20))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        Form.setFont(font)
        Form.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.clockLabel = QtWidgets.QLabel(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        self.clockLabel.setFont(font)
        self.clockLabel.setStyleSheet("")
        self.clockLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.clockLabel.setObjectName("clockLabel")
        self.gridLayout.addWidget(self.clockLabel, 0, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.clockLabel.setText(_translate("Form", "00:00"))
