# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\component\basiccomp\clocksetcomp.ui'
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
        Form.setStyleSheet("background-color: #242325;\n"
"")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 30))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    background-color: #4357AD;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: none;\n"
"    background-color: #213aa6;\n"
"    color: white;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 2)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: white;\n"
"background-color: #474646;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "SET"))
        self.lineEdit.setInputMask(_translate("Form", "00:00"))
        self.lineEdit.setText(_translate("Form", "00:00"))
