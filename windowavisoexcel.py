# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowavisoexcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowavisoexcel(object):
    def setupUi(self, windowavisoexcel):
        windowavisoexcel.setObjectName("windowavisoexcel")
        windowavisoexcel.setWindowModality(QtCore.Qt.WindowModal)
        windowavisoexcel.resize(400, 300)
        self.buttonBox = QtWidgets.QDialogButtonBox(windowavisoexcel)
        self.buttonBox.setGeometry(QtCore.QRect(120, 250, 160, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(windowavisoexcel)
        self.label.setGeometry(QtCore.QRect(136, 30, 128, 128))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/avisoexcel/avisoexcel.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(windowavisoexcel)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 380, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(windowavisoexcel)
        self.buttonBox.accepted.connect(windowavisoexcel.accept) # type: ignore
        self.buttonBox.rejected.connect(windowavisoexcel.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(windowavisoexcel)

    def retranslateUi(self, windowavisoexcel):
        _translate = QtCore.QCoreApplication.translate
        windowavisoexcel.setWindowTitle(_translate("windowavisoexcel", "Aviso - Cargar datos desde excel"))
        self.label_2.setText(_translate("windowavisoexcel", "¿Desea guardar la información del archivo en la base de datos?"))
import avisoexcel_rc