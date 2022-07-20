# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gestion.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 821)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 791, 741))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_clientes = QtWidgets.QWidget()
        self.tab_clientes.setObjectName("tab_clientes")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_clientes)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(390, 210, 328, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_pago = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_pago.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_pago.setSpacing(10)
        self.horizontalLayout_pago.setObjectName("horizontalLayout_pago")
        self.labelpago = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.labelpago.setObjectName("labelpago")
        self.horizontalLayout_pago.addWidget(self.labelpago)
        self.chkEfectivo = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkEfectivo.setObjectName("chkEfectivo")
        self.rbtGroupPago = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupPago.setObjectName("rbtGroupPago")
        self.rbtGroupPago.setExclusive(False)
        self.rbtGroupPago.addButton(self.chkEfectivo)
        self.horizontalLayout_pago.addWidget(self.chkEfectivo)
        self.chkTarjeta = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTarjeta.setObjectName("chkTarjeta")
        self.rbtGroupPago.addButton(self.chkTarjeta)
        self.horizontalLayout_pago.addWidget(self.chkTarjeta)
        self.chkTransferencia = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.chkTransferencia.setObjectName("chkTransferencia")
        self.rbtGroupPago.addButton(self.chkTransferencia)
        self.horizontalLayout_pago.addWidget(self.chkTransferencia)
        self.lineEdit_apellido = QtWidgets.QLineEdit(self.tab_clientes)
        self.lineEdit_apellido.setGeometry(QtCore.QRect(150, 120, 113, 20))
        self.lineEdit_apellido.setObjectName("lineEdit_apellido")
        self.label_dni_valid = QtWidgets.QLabel(self.tab_clientes)
        self.label_dni_valid.setGeometry(QtCore.QRect(260, 10, 31, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_dni_valid.setFont(font)
        self.label_dni_valid.setText("")
        self.label_dni_valid.setObjectName("label_dni_valid")
        self.lineEdit_dni = QtWidgets.QLineEdit(self.tab_clientes)
        self.lineEdit_dni.setGeometry(QtCore.QRect(140, 20, 113, 20))
        self.lineEdit_dni.setObjectName("lineEdit_dni")
        self.label_direccion = QtWidgets.QLabel(self.tab_clientes)
        self.label_direccion.setGeometry(QtCore.QRect(100, 165, 47, 13))
        self.label_direccion.setObjectName("label_direccion")
        self.lineEdit_direccion = QtWidgets.QLineEdit(self.tab_clientes)
        self.lineEdit_direccion.setGeometry(QtCore.QRect(150, 160, 113, 20))
        self.lineEdit_direccion.setObjectName("lineEdit_direccion")
        self.line_abajo = QtWidgets.QFrame(self.tab_clientes)
        self.line_abajo.setGeometry(QtCore.QRect(40, 680, 701, 16))
        self.line_abajo.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_abajo.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_abajo.setObjectName("line_abajo")
        self.label_nombre = QtWidgets.QLabel(self.tab_clientes)
        self.label_nombre.setGeometry(QtCore.QRect(500, 130, 47, 13))
        self.label_nombre.setObjectName("label_nombre")
        self.label_prov = QtWidgets.QLabel(self.tab_clientes)
        self.label_prov.setGeometry(QtCore.QRect(500, 170, 47, 13))
        self.label_prov.setObjectName("label_prov")
        self.cmbProv = QtWidgets.QComboBox(self.tab_clientes)
        self.cmbProv.setGeometry(QtCore.QRect(550, 165, 113, 22))
        self.cmbProv.setObjectName("cmbProv")
        self.label_fecha_alta = QtWidgets.QLabel(self.tab_clientes)
        self.label_fecha_alta.setGeometry(QtCore.QRect(500, 25, 61, 16))
        self.label_fecha_alta.setObjectName("label_fecha_alta")
        self.label_apellido = QtWidgets.QLabel(self.tab_clientes)
        self.label_apellido.setGeometry(QtCore.QRect(100, 125, 47, 13))
        self.label_apellido.setObjectName("label_apellido")
        self.label_dni = QtWidgets.QLabel(self.tab_clientes)
        self.label_dni.setGeometry(QtCore.QRect(90, 25, 47, 13))
        self.label_dni.setObjectName("label_dni")
        self.lineEdit_nombre = QtWidgets.QLineEdit(self.tab_clientes)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(550, 125, 113, 20))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")
        self.lineEdit_fecha = QtWidgets.QLineEdit(self.tab_clientes)
        self.lineEdit_fecha.setGeometry(QtCore.QRect(570, 20, 101, 20))
        self.lineEdit_fecha.setObjectName("lineEdit_fecha")
        self.pushButtonCalendar = QtWidgets.QPushButton(self.tab_clientes)
        self.pushButtonCalendar.setGeometry(QtCore.QRect(680, 10, 32, 32))
        self.pushButtonCalendar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/calendar/calendar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCalendar.setIcon(icon)
        self.pushButtonCalendar.setObjectName("pushButtonCalendar")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_clientes)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(150, 210, 199, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_sexo = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_sexo.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_sexo.setObjectName("horizontalLayout_sexo")
        self.labelsexo = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelsexo.setFont(font)
        self.labelsexo.setObjectName("labelsexo")
        self.horizontalLayout_sexo.addWidget(self.labelsexo)
        self.rbtFem = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtFem.setAutoExclusive(False)
        self.rbtFem.setObjectName("rbtFem")
        self.rbtGroupSex = QtWidgets.QButtonGroup(MainWindow)
        self.rbtGroupSex.setObjectName("rbtGroupSex")
        self.rbtGroupSex.addButton(self.rbtFem)
        self.horizontalLayout_sexo.addWidget(self.rbtFem)
        self.rbtMas = QtWidgets.QRadioButton(self.horizontalLayoutWidget)
        self.rbtMas.setAutoExclusive(False)
        self.rbtMas.setObjectName("rbtMas")
        self.rbtGroupSex.addButton(self.rbtMas)
        self.horizontalLayout_sexo.addWidget(self.rbtMas)
        self.tableClientes = QtWidgets.QTableWidget(self.tab_clientes)
        self.tableClientes.setGeometry(QtCore.QRect(40, 320, 701, 271))
        self.tableClientes.setColumnCount(3)
        self.tableClientes.setObjectName("tableClientes")
        self.tableClientes.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableClientes.setHorizontalHeaderItem(2, item)
        self.lblstatus = QtWidgets.QLabel(self.tab_clientes)
        self.lblstatus.setGeometry(QtCore.QRect(40, 650, 701, 31))
        self.lblstatus.setText("")
        self.lblstatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblstatus.setObjectName("lblstatus")
        self.label_codigo = QtWidgets.QLabel(self.tab_clientes)
        self.label_codigo.setGeometry(QtCore.QRect(20, 20, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_codigo.setFont(font)
        self.label_codigo.setStyleSheet("color: rgb(0, 170, 255);")
        self.label_codigo.setText("")
        self.label_codigo.setObjectName("label_codigo")
        self.Buscar = QtWidgets.QPushButton(self.tab_clientes)
        self.Buscar.setGeometry(QtCore.QRect(300, 10, 32, 32))
        self.Buscar.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/lupa/lupa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Buscar.setIcon(icon1)
        self.Buscar.setObjectName("Buscar")
        self.Recargar = QtWidgets.QPushButton(self.tab_clientes)
        self.Recargar.setGeometry(QtCore.QRect(340, 10, 32, 32))
        self.Recargar.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/reload/reload.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Recargar.setIcon(icon2)
        self.Recargar.setObjectName("Recargar")
        self.layoutWidget = QtWidgets.QWidget(self.tab_clientes)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 600, 701, 51))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_botones_inferiores = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_botones_inferiores.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_botones_inferiores.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_botones_inferiores.setSpacing(10)
        self.horizontalLayout_botones_inferiores.setObjectName("horizontalLayout_botones_inferiores")
        self.Alta = QtWidgets.QPushButton(self.layoutWidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/alta/alta.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Alta.setIcon(icon3)
        self.Alta.setObjectName("Alta")
        self.horizontalLayout_botones_inferiores.addWidget(self.Alta)
        self.Modificar = QtWidgets.QPushButton(self.layoutWidget)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/modificar/modificar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Modificar.setIcon(icon4)
        self.Modificar.setObjectName("Modificar")
        self.horizontalLayout_botones_inferiores.addWidget(self.Modificar)
        self.Eliminar = QtWidgets.QPushButton(self.layoutWidget)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/eliminar/eliminar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Eliminar.setIcon(icon5)
        self.Eliminar.setObjectName("Eliminar")
        self.horizontalLayout_botones_inferiores.addWidget(self.Eliminar)
        self.Limpiar = QtWidgets.QPushButton(self.layoutWidget)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/limpiar/limpiar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Limpiar.setIcon(icon6)
        self.Limpiar.setObjectName("Limpiar")
        self.horizontalLayout_botones_inferiores.addWidget(self.Limpiar)
        self.pushButton_Salir = QtWidgets.QPushButton(self.layoutWidget)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/salir/salir.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Salir.setIcon(icon7)
        self.pushButton_Salir.setObjectName("pushButton_Salir")
        self.horizontalLayout_botones_inferiores.addWidget(self.pushButton_Salir)
        self.labelstatusbar = QtWidgets.QLabel(self.tab_clientes)
        self.labelstatusbar.setGeometry(QtCore.QRect(10, 690, 47, 13))
        self.labelstatusbar.setText("")
        self.labelstatusbar.setObjectName("labelstatusbar")
        self.spinBoxEnvio = QtWidgets.QSpinBox(self.tab_clientes)
        self.spinBoxEnvio.setGeometry(QtCore.QRect(590, 65, 42, 22))
        self.spinBoxEnvio.setMaximum(3)
        self.spinBoxEnvio.setObjectName("spinBoxEnvio")
        self.label_envio = QtWidgets.QLabel(self.tab_clientes)
        self.label_envio.setGeometry(QtCore.QRect(500, 70, 91, 16))
        self.label_envio.setObjectName("label_envio")
        self.label_envio_valor = QtWidgets.QLabel(self.tab_clientes)
        self.label_envio_valor.setGeometry(QtCore.QRect(500, 100, 251, 16))
        self.label_envio_valor.setAlignment(QtCore.Qt.AlignCenter)
        self.label_envio_valor.setObjectName("label_envio_valor")
        self.tabWidget.addTab(self.tab_clientes, "")
        self.tab_facturacion = QtWidgets.QWidget()
        self.tab_facturacion.setObjectName("tab_facturacion")
        self.tabWidget.addTab(self.tab_facturacion, "")
        self.tab_productos = QtWidgets.QWidget()
        self.tab_productos.setObjectName("tab_productos")
        self.tabWidget.addTab(self.tab_productos, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 21))
        self.menubar.setObjectName("menubar")
        self.menuArchivo = QtWidgets.QMenu(self.menubar)
        self.menuArchivo.setObjectName("menuArchivo")
        MainWindow.setMenuBar(self.menubar)
        self.toolBarHerramientas = QtWidgets.QToolBar(MainWindow)
        self.toolBarHerramientas.setObjectName("toolBarHerramientas")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBarHerramientas)
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.actionCrtl_S = QtWidgets.QAction(MainWindow)
        self.actionCrtl_S.setObjectName("actionCrtl_S")
        self.actionAbrir = QtWidgets.QAction(MainWindow)
        self.actionAbrir.setObjectName("actionAbrir")
        self.actionComprimirZip = QtWidgets.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/zip/zip.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionComprimirZip.setIcon(icon8)
        self.actionComprimirZip.setObjectName("actionComprimirZip")
        self.actionrestaurarBd = QtWidgets.QAction(MainWindow)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/restore/restore.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionrestaurarBd.setIcon(icon9)
        self.actionrestaurarBd.setObjectName("actionrestaurarBd")
        self.actionimportarExcel = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/excel/excel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionimportarExcel.setIcon(icon10)
        self.actionimportarExcel.setObjectName("actionimportarExcel")
        self.actioninformenpdf = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/informepdf/informe-pdf.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actioninformenpdf.setIcon(icon11)
        self.actioninformenpdf.setObjectName("actioninformenpdf")
        self.menuArchivo.addAction(self.actionAbrir)
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionSalir)
        self.menubar.addAction(self.menuArchivo.menuAction())
        self.toolBarHerramientas.addAction(self.actionComprimirZip)
        self.toolBarHerramientas.addAction(self.actionrestaurarBd)
        self.toolBarHerramientas.addAction(self.actionimportarExcel)
        self.toolBarHerramientas.addAction(self.actioninformenpdf)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelpago.setText(_translate("MainWindow", "Métodos de Pago:"))
        self.chkEfectivo.setText(_translate("MainWindow", "Efectivo"))
        self.chkTarjeta.setText(_translate("MainWindow", "Tarjeta"))
        self.chkTransferencia.setText(_translate("MainWindow", "Transferencia"))
        self.label_direccion.setText(_translate("MainWindow", "Dirección:"))
        self.label_nombre.setText(_translate("MainWindow", "Nombre:"))
        self.label_prov.setText(_translate("MainWindow", "Provincia:"))
        self.label_fecha_alta.setText(_translate("MainWindow", "Fecha Alta:"))
        self.label_apellido.setText(_translate("MainWindow", "Apellido:"))
        self.label_dni.setText(_translate("MainWindow", "DNI:"))
        self.labelsexo.setText(_translate("MainWindow", "Sexo:"))
        self.rbtFem.setText(_translate("MainWindow", "Femenino"))
        self.rbtMas.setText(_translate("MainWindow", "Masculino"))
        item = self.tableClientes.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "DNI"))
        item = self.tableClientes.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Apellidos"))
        item = self.tableClientes.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Nombre"))
        self.Alta.setText(_translate("MainWindow", "Alta"))
        self.Modificar.setText(_translate("MainWindow", "Modificar"))
        self.Eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.Limpiar.setText(_translate("MainWindow", "Limpiar"))
        self.pushButton_Salir.setText(_translate("MainWindow", "Salir"))
        self.label_envio.setText(_translate("MainWindow", "Forma de envío:"))
        self.label_envio_valor.setText(_translate("MainWindow", "Recogida por cliente"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_clientes), _translate("MainWindow", "Clientes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_facturacion), _translate("MainWindow", "Facturación"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_productos), _translate("MainWindow", "Productos"))
        self.menuArchivo.setTitle(_translate("MainWindow", "Archivo"))
        self.toolBarHerramientas.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))
        self.actionSalir.setShortcut(_translate("MainWindow", "Alt+4"))
        self.actionCrtl_S.setText(_translate("MainWindow", "Abrir..."))
        self.actionCrtl_S.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir..."))
        self.actionComprimirZip.setText(_translate("MainWindow", "ComprimirZip"))
        self.actionComprimirZip.setToolTip(_translate("MainWindow", "Comprimir Base de Datos a ZIP"))
        self.actionrestaurarBd.setText(_translate("MainWindow", "restaurarBd"))
        self.actionrestaurarBd.setToolTip(_translate("MainWindow", "Restaurar Base de Datos"))
        self.actionimportarExcel.setText(_translate("MainWindow", "importarExcel"))
        self.actionimportarExcel.setToolTip(_translate("MainWindow", "Cargar datos desde Excel"))
        self.actioninformenpdf.setText(_translate("MainWindow", "informenpdf"))
import alta_rc
import calendar_rc
import eliminar_rc
import excel_rc
import informepdf_rc
import limpiar_rc
import lupa_rc
import modificar_rc
import reload_rc
import restore_rc
import salir_rc
import zip_rc
