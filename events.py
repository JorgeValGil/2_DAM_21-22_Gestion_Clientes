import os.path
import shutil
import zipfile
from datetime import date
from datetime import datetime

import xlrd
from PyQt5 import QtWidgets
import conexion
import sys
import var


class Eventos:

    def Salir(self):
        try:
            var.dlgsalir.show()
            if var.dlgsalir.exec():
                sys.exit()
            else:
                var.dlgsalir.hide()
        except Exception as error:
            print('Error en módulo salir ', error)

    def SalirArchivo(self):
        try:
            sys.exit()
        except Exception as error:
            print("Error %s: " % str(error))

    def StatusBar(self):
        var.ui.statusbar.addPermanentWidget(var.ui.labelstatusbar, 1)
        today = date.today()
        todayformat = today.strftime("%d/%m/%Y")
        var.ui.labelstatusbar.setText(todayformat)

    def AbrirDir(self):
        try:
            var.filedlgabrir.show()
        except Exception as error:
            print("Error abrir explorador: %s" % str(error))

    def Backup():
        try:
            fecha = datetime.today()
            fecha = fecha.strftime('%Y.%m.%d.%H.%M.%S')
            var.copia = (str(fecha) + '_backup.zip')
            option = QtWidgets.QFileDialog.Options()
            directorio, filename = var.filedlgabrir.getSaveFileName(None, 'Guardar Copia', var.copia, '.zip',
                                                                    options=option)
            if var.filedlgabrir.Accepted and filename != '':
                fichzip = zipfile.ZipFile(var.copia, 'w')
                fichzip.write(var.filebd, os.path.basename(var.filebd), zipfile.ZIP_DEFLATED)
                fichzip.close()
                var.ui.labelstatusbar.setText('BASE DE DATOS CREADA')
                shutil.move(str(var.copia), str(directorio))
        except Exception as error:
            print("Error %s: " % str(error))

    def Restore():
        try:
            ventana_restaurar = QtWidgets.QFileDialog
            filename, filtro = ventana_restaurar.getOpenFileName(None, 'Restaurar Copia', "Copia de seguridad BD",
                                                                 "Archivos Zip (*.zip)")
            print(filename)
            nombre_archivo_con_extension = os.path.basename(filename)
            nombre_archivo = nombre_archivo_con_extension[:-4]
            if ventana_restaurar.Accepted and filename != '':
                fichzip = zipfile.ZipFile(filename, 'r')
                fichzip.extractall(nombre_archivo)
                print(os.path.dirname(os.path.realpath(__file__)) + "\\" + nombre_archivo + "\\" + var.filebd)
                shutil.move(os.path.dirname(os.path.realpath(__file__)) + "\\" + nombre_archivo + "\\" + var.filebd,
                            os.path.dirname(os.path.realpath(__file__)) + "\\" + var.filebd)
                shutil.rmtree(os.path.dirname(os.path.realpath(__file__)) + "\\" + nombre_archivo)
                conexion.Conexion.mostrarClientes()
                fichzip.close()
                var.ui.labelstatusbar.setText('BASE DE DATOS ' + nombre_archivo + ' RESTAURADA')
        except Exception as error:
            print("Error %s: " % str(error))

    def Excel():
        try:
            var.dlgexcel.show()
            if var.dlgexcel.exec():
                var.dlgexcel.hide()
                return True
            else:
                var.dlgexcel.hide()
                return False
        except Exception as error:
            print('Error en módulo salir ', error)

    def cargarExcel():
        try:
            ventana_cargar = QtWidgets.QFileDialog
            filename, filtro = ventana_cargar.getOpenFileName(None, 'Cargar datos desde Excel', "Datos Excel",
                                                              "Archivos Excel (*.xls)")
            archivo_excel = xlrd.open_workbook(filename)
            hoja = archivo_excel.sheet_by_index(0)
            filas = hoja.nrows
            columnas = hoja.ncols
            if Eventos.Excel():
                for i in range(filas):
                    if i != 0:
                        newcli = []
                        dni = hoja.cell_value(i, 0)
                        for j in range(columnas):
                            if j == 8:
                                newcli.append(int(hoja.cell_value(i, j)))
                            else:
                                newcli.append(hoja.cell_value(i, j))
                        if conexion.Conexion.buscarCliExcel(dni):
                            conexion.Conexion.modifCliExcel(newcli)
                        else:
                            conexion.Conexion.cargarCli(newcli)
        except Exception as error:
            print("Error %s: " % str(error))
