# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\window\ui\startmenu.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(638, 527)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.listWidget.setFont(font)
        self.listWidget.setIconSize(QtCore.QSize(60, 60))
        self.listWidget.setFlow(QtWidgets.QListView.Flow.LeftToRight)
        self.listWidget.setProperty("isWrapping", False)
        self.listWidget.setGridSize(QtCore.QSize(120, 100))
        self.listWidget.setViewMode(QtWidgets.QListView.ViewMode.IconMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setWordWrap(True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 1, 0, 1, 2)
        self.treeWidget = QtWidgets.QTreeWidget(parent=Form)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setTextAlignment(0, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(1, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(2, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(3, QtCore.Qt.AlignmentFlag.AlignCenter)
        self.treeWidget.headerItem().setTextAlignment(4, QtCore.Qt.AlignmentFlag.AlignCenter)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.gridLayout.addWidget(self.treeWidget, 2, 0, 1, 2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Welcome to TeleScore"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "File Name"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Author"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Version Number"))
        self.treeWidget.headerItem().setText(3, _translate("Form", "File Location"))
        self.treeWidget.headerItem().setText(4, _translate("Form", "Date Modified"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Form", "Open Existing File"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
