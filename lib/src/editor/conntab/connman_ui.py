# Form implementation generated from reading ui file 'c:\Users\riscyseven\TeleScore\build\exe.win-amd64-3.11\lib\src\editor\conntab\connman.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(393, 210)
        Form.setMaximumSize(QtCore.QSize(16777215, 300))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.treeWidget_2 = QtWidgets.QTreeWidget(parent=Form)
        self.treeWidget_2.setMaximumSize(QtCore.QSize(16777215, 120))
        self.treeWidget_2.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.treeWidget_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.treeWidget_2.setRootIsDecorated(False)
        self.treeWidget_2.setItemsExpandable(False)
        self.treeWidget_2.setExpandsOnDoubleClick(False)
        self.treeWidget_2.setObjectName("treeWidget_2")
        self.gridLayout.addWidget(self.treeWidget_2, 3, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(parent=Form)
        self.treeWidget.setMaximumSize(QtCore.QSize(16777215, 140))
        self.treeWidget.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.treeWidget.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.treeWidget.setIndentation(0)
        self.treeWidget.setRootIsDecorated(False)
        self.treeWidget.setItemsExpandable(False)
        self.treeWidget.setExpandsOnDoubleClick(False)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.header().setVisible(True)
        self.treeWidget.header().setMinimumSectionSize(0)
        self.treeWidget.header().setStretchLastSection(True)
        self.gridLayout.addWidget(self.treeWidget, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "(Point B Connections)"))
        self.treeWidget_2.headerItem().setText(0, _translate("Form", "-"))
        self.treeWidget_2.headerItem().setText(1, _translate("Form", "Action"))
        self.treeWidget_2.headerItem().setText(2, _translate("Form", "Component"))
        self.treeWidget.headerItem().setText(0, _translate("Form", "-"))
        self.treeWidget.headerItem().setText(1, _translate("Form", "Action"))
        self.treeWidget.headerItem().setText(2, _translate("Form", "Component"))
        self.label_2.setText(_translate("Form", "(Point A Connections)"))