# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\editor\proptab\fileseldialog.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ActionDialog(object):
    def setupUi(self, ActionDialog):
        ActionDialog.setObjectName("ActionDialog")
        ActionDialog.resize(210, 30)
        ActionDialog.setMinimumSize(QtCore.QSize(0, 0))
        self.gridLayout = QtWidgets.QGridLayout(ActionDialog)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.absPathButton = QtWidgets.QPushButton(parent=ActionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.absPathButton.sizePolicy().hasHeightForWidth())
        self.absPathButton.setSizePolicy(sizePolicy)
        self.absPathButton.setMinimumSize(QtCore.QSize(20, 0))
        self.absPathButton.setMaximumSize(QtCore.QSize(20, 16777215))
        self.absPathButton.setObjectName("absPathButton")
        self.gridLayout.addWidget(self.absPathButton, 0, 2, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(parent=ActionDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.clrButton = QtWidgets.QPushButton(parent=ActionDialog)
        self.clrButton.setMinimumSize(QtCore.QSize(0, 0))
        self.clrButton.setMaximumSize(QtCore.QSize(50, 16777215))
        self.clrButton.setObjectName("clrButton")
        self.gridLayout.addWidget(self.clrButton, 0, 1, 1, 1)

        self.retranslateUi(ActionDialog)
        QtCore.QMetaObject.connectSlotsByName(ActionDialog)

    def retranslateUi(self, ActionDialog):
        _translate = QtCore.QCoreApplication.translate
        ActionDialog.setWindowTitle(_translate("ActionDialog", "Dialog"))
        self.absPathButton.setText(_translate("ActionDialog", "..."))
        self.clrButton.setText(_translate("ActionDialog", "Clear"))