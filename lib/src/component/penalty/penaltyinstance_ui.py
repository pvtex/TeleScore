# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\component\penalty\penaltyinstance.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_PenaltyInstance(object):
    def setupUi(self, PenaltyInstance):
        PenaltyInstance.setObjectName("PenaltyInstance")
        PenaltyInstance.setEnabled(True)
        PenaltyInstance.resize(298, 54)
        PenaltyInstance.setMinimumSize(QtCore.QSize(0, 40))
        PenaltyInstance.setStyleSheet("QLineEdit {\n"
"    color: white;\n"
"    background-color: #808080;\n"
"    border: none;\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background-color: #474646;\n"
"}")
        self.gridLayout = QtWidgets.QGridLayout(PenaltyInstance)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        self.edit_pushButton = QtWidgets.QPushButton(parent=PenaltyInstance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_pushButton.sizePolicy().hasHeightForWidth())
        self.edit_pushButton.setSizePolicy(sizePolicy)
        self.edit_pushButton.setMinimumSize(QtCore.QSize(50, 0))
        self.edit_pushButton.setMaximumSize(QtCore.QSize(40, 16777215))
        self.edit_pushButton.setObjectName("edit_pushButton")
        self.gridLayout.addWidget(self.edit_pushButton, 0, 3, 1, 1)
        self.plyr_lineEdit = QtWidgets.QLineEdit(parent=PenaltyInstance)
        self.plyr_lineEdit.setEnabled(False)
        self.plyr_lineEdit.setObjectName("plyr_lineEdit")
        self.gridLayout.addWidget(self.plyr_lineEdit, 0, 1, 1, 1)
        self.rem_pushButton = QtWidgets.QPushButton(parent=PenaltyInstance)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rem_pushButton.sizePolicy().hasHeightForWidth())
        self.rem_pushButton.setSizePolicy(sizePolicy)
        self.rem_pushButton.setMinimumSize(QtCore.QSize(60, 0))
        self.rem_pushButton.setMaximumSize(QtCore.QSize(50, 60))
        self.rem_pushButton.setObjectName("rem_pushButton")
        self.gridLayout.addWidget(self.rem_pushButton, 0, 4, 1, 1)
        self.time_lineEdit = QtWidgets.QLineEdit(parent=PenaltyInstance)
        self.time_lineEdit.setEnabled(False)
        self.time_lineEdit.setObjectName("time_lineEdit")
        self.gridLayout.addWidget(self.time_lineEdit, 0, 2, 1, 1)

        self.retranslateUi(PenaltyInstance)
        QtCore.QMetaObject.connectSlotsByName(PenaltyInstance)

    def retranslateUi(self, PenaltyInstance):
        _translate = QtCore.QCoreApplication.translate
        PenaltyInstance.setWindowTitle(_translate("PenaltyInstance", "Form"))
        self.edit_pushButton.setText(_translate("PenaltyInstance", "Edit"))
        self.rem_pushButton.setText(_translate("PenaltyInstance", "Remove"))
        self.time_lineEdit.setInputMask(_translate("PenaltyInstance", "99:99"))
        self.time_lineEdit.setText(_translate("PenaltyInstance", "00:00"))