from datetime import *
import Printer
import clients
import conexion
import events
import sys
import var
from calendario import *
from gestion import *
from windowaviso import *
from windowavisoexcel import *


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.SalirArchivo)
        var.ui.actionAbrir.triggered.connect(events.Eventos.AbrirDir)
        var.ui.actionComprimirZip.triggered.connect(events.Eventos.Backup)
        var.ui.actionrestaurarBd.triggered.connect(events.Eventos.Restore)
        var.ui.actionimportarExcel.triggered.connect(events.Eventos.cargarExcel)
        var.ui.actioninformenpdf.triggered.connect(Printer.Printer.reportCli)
        var.ui.lineEdit_dni.editingFinished.connect(clients.Clientes.validarDNI)

        var.ui.rbtGroupSex.buttonClicked.connect(clients.Clientes.selSexo)

        var.ui.rbtGroupPago.buttonClicked.connect(clients.Clientes.selPago)

        clients.Clientes.cargarProv()
        var.ui.cmbProv.activated[str].connect(clients.Clientes.selProv)
        var.ui.pushButtonCalendar.clicked.connect(clients.Clientes.abrirCalendar)

        var.ui.Alta.clicked.connect(clients.Clientes.altaClientes)
        var.ui.Eliminar.clicked.connect(clients.Clientes.bajaCliente)
        var.ui.Limpiar.clicked.connect(clients.Clientes.limpiarCli)
        var.ui.Recargar.clicked.connect(conexion.Conexion.mostrarClientes)
        var.ui.Buscar.clicked.connect(clients.Clientes.buscarCliente)
        var.ui.Modificar.clicked.connect(clients.Clientes.modifCliente)
        conexion.Conexion.db_connect(var.filebd)
        conexion.Conexion.mostrarClientes()

        for i in range(var.ui.tableClientes.horizontalHeader().count()):
            var.ui.tableClientes.horizontalHeader().setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)

        events.Eventos.StatusBar(self)
        var.ui.spinBoxEnvio.valueChanged.connect(clients.Clientes.selEnvioLabel)


class DialogSalir(QtWidgets.QDialog):
    def __init__(self):
        super(DialogSalir, self).__init__()
        var.dlgsalir = Ui_windowaviso()
        var.dlgsalir.setupUi(self)
        var.ui.pushButton_Salir.clicked.connect(events.Eventos.Salir)


class DialogExcel(QtWidgets.QDialog):
    def __init__(self):
        super(DialogExcel, self).__init__()
        var.dlgexcel = Ui_windowavisoexcel()
        var.dlgexcel.setupUi(self)


class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_venCalendar()
        var.dlgcalendar.setupUi(self)
        var.filedlgabrir = FileDIalogAbrir()
        diaactual = datetime.now().day
        mesactual = datetime.now().month
        anoactual = datetime.now().year
        var.dlgcalendar.Calendar.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.Calendar.clicked.connect(clients.Clientes.cargarFecha)


class FileDIalogAbrir(QtWidgets.QFileDialog):
    def __init__(self):
        super(FileDIalogAbrir, self).__init__()


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.dlgsalir = DialogSalir()
    var.dlgcalendar = DialogCalendar()
    var.dlgexcel = DialogExcel()
    window.show()
    sys.exit(app.exec())
