# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\editor\complisttab.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_yay(object):
    def setupUi(self, yay):
        yay.setObjectName("yay")
        yay.resize(300, 204)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(yay.sizePolicy().hasHeightForWidth())
        yay.setSizePolicy(sizePolicy)
        yay.setMinimumSize(QtCore.QSize(300, 0))
        self.gridLayout = QtWidgets.QGridLayout(yay)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget = QtWidgets.QTreeWidget(parent=yay)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setIconSize(QtCore.QSize(50, 50))
        self.treeWidget.setIndentation(0)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.treeWidget.headerItem().setText(1, "2")
        self.treeWidget.header().setVisible(False)
        self.gridLayout.addWidget(self.treeWidget, 0, 0, 1, 1)

        self.retranslateUi(yay)
        QtCore.QMetaObject.connectSlotsByName(yay)

    def retranslateUi(self, yay):
        _translate = QtCore.QCoreApplication.translate
        yay.setWindowTitle(_translate("yay", "Form"))
