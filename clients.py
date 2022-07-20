from PyQt5 import QtCore, QtWidgets

import conexion
import var


class Clientes:

    def validarDNI():
        try:
            dni = var.ui.lineEdit_dni.text()
            var.ui.lineEdit_dni.setText(dni.upper())
            tabla = 'TRWAGMYFPDXBNJZSQVHLCKE'  # letras dni
            dig_ext = 'XYZ'  # dígito
            reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '1234567890'
            dni = dni.upper()  # conver la letra mayúscula
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
                if len(dni) == len([n for n in dni if n in numeros]) and tabla[int(dni) % 23] == dig_control:
                    var.ui.label_dni_valid.setStyleSheet('QLabel {color: green;}')
                    var.ui.label_dni_valid.setText('V')
                else:
                    var.ui.label_dni_valid.setStyleSheet('QLabel {color: red;}')
                    var.ui.label_dni_valid.setText('X')
            else:
                var.ui.label_dni_valid.setStyleSheet('QLabel {color: red;}')
                var.ui.label_dni_valid.setText('X')
        except Exception as error:
            print('Error en módulo validar DNI', error)

    def cargarProv():
        try:
            prov = ['', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra']
            var.datosprovincias = prov
            for i in prov:
                var.ui.cmbProv.addItem(i)
        except Exception as error:
            print('Error: %s' % str(error))

    def selProv(prov):
        try:
            var.vpro = prov
            print('Has seleccionado la provincia de ', prov)
            # return prov;
        except Exception as error:
            print('Error: %s' % str(error))

    def selSexo(self):
        try:
            if var.ui.rbtFem.isChecked():
                var.sex = 'Mujer'
            if var.ui.rbtMas.isChecked():
                var.sex = 'Hombre'
        except Exception as error:
            print('Error en módulo seleccionar sexo:', error)

    def selPago():
        try:
            var.pay = []
            for i, data in enumerate(var.ui.rbtGroupPago.buttons()):
                # agrupamos en QtDesigner los checkbox en ButtonGroup
                if var.ui.chkEfectivo.isChecked() and i == 0:
                    print('pagas con efectivo')
                    var.pay.append("Efectivo")
                if var.ui.chkTarjeta.isChecked() and i == 1:
                    print('pagas con tarjeta')
                    var.pay.append("Tarjeta")
                if var.ui.chkTransferencia.isChecked() and i == 2:
                    print('pagas con transferencia')
                    var.pay.append("Transferencia")
            # var.pay = set(var.pay)
            print(var.pay)
            return var.pay
        except Exception as error:
            print('Error: %s' % str(error))

    def abrirCalendar():
        try:
            var.dlgcalendar.show()
        except Exception as error:
            print('Error: %s ' % str(error))

    def cargarFecha(qDate):
        try:
            data = ('{0}/{1}/{2}'.format(qDate.day(), qDate.month(), qDate.year()))
            var.ui.lineEdit_fecha.setText(str(data))
            var.dlgcalendar.hide()
        except Exception as error:
            print('Error cargar fecha: %s' % str(error))

    def altaClientes():
        try:
            if (var.ui.lineEdit_dni == '' or var.ui.lineEdit_apellido == '' or var.ui.lineEdit_nombre == ''
                    or var.ui.lineEdit_fecha == '' or var.ui.lineEdit_direccion == ''
                    or str(var.ui.spinBoxEnvio.value()) == ''):
                print('Faltan datos')
            else:
                # Preparamos el registro
                newcli = []
                clitab = []  # serán los datos que carguemos en la tabla
                client = [var.ui.lineEdit_dni, var.ui.lineEdit_apellido, var.ui.lineEdit_nombre, var.ui.lineEdit_fecha,
                          var.ui.lineEdit_direccion]
                k = 0
                for i in client:
                    newcli.append(i.text())
                    # carguemos los valores para la tabla que solo tiene tres DNI, apellidos y nombre
                    if k < 3:
                        clitab.append(i.text())
                        k += 1
                newcli.append(var.vpro)
                var.pay2 = Clientes.selPago()
                newcli.append(var.sex)
                newcli.append(var.pay2)
                newcli.append(str(var.ui.spinBoxEnvio.value()))
                if client:
                    # comprobamos que no esté vacío lo principal
                    # aqui empieza como trabajar con la TableWidget
                    row = 0  # posicion de la fila, problema: coloca al último como el primero en cada click
                    column = 0  # posicion de la columna
                    var.ui.tableClientes.insertRow(row)  # insertamos una fila nueva con cada click de botón
                    for registro in clitab:
                        # la celda tiene una posicion fila, columna y cargamos en ella el dato
                        cell = QtWidgets.QTableWidgetItem(registro)  # carga en cell dato de la lista
                        var.ui.tableClientes.setItem(row, column, cell)  # lo escribe
                        column += 1
                    conexion.Conexion.cargarCli(newcli)
                else:
                    print('Faltan datos')
                # Clientes.limpiarCli(client, var.rbtsex, var.chkpago)
                Clientes.limpiarCliNoEstado()
                # conexion.Conexion.cargarCli(newcli)
        except Exception as error:
            print('Error: %s' % str(error))

    def bajaCliente():
        try:
            if (var.ui.lineEdit_dni.text().strip() != ''):
                dni = var.ui.lineEdit_dni.text()
                conexion.Conexion.bajaCli(dni)
                conexion.Conexion.mostrarClientes()
                Clientes.limpiarCliNoEstado()
            else:
                var.ui.lblstatus.setText('Error al Eliminar! El campo de texto "DNI" no puede estar vacío.')
        except Exception as error:
            print('Error al eliminar el cliente: %s' % str(error))

    def modifCliente(self):
        try:
            newdata = []
            client = [var.ui.lineEdit_dni, var.ui.lineEdit_apellido, var.ui.lineEdit_nombre, var.ui.lineEdit_fecha,
                      var.ui.lineEdit_direccion]
            for i in client:
                newdata.append(i.text())

            newdata.append(var.ui.cmbProv.currentText())

            sexo = ''
            if var.ui.rbtFem.isChecked():
                sexo = 'Mujer'
            if var.ui.rbtMas.isChecked():
                sexo = 'Hombre'
            newdata.append(sexo)

            var.pay = Clientes.selPago()
            newdata.append(var.pay)
            envio = var.ui.spinBoxEnvio.value()
            newdata.append(envio)
            print(newdata)
            cod = var.ui.label_codigo.text()
            conexion.Conexion.modifCli(cod, newdata)
            conexion.Conexion.mostrarClientes()

        except Exception as error:
            print('Error cargar clientes: %s ' % str(error))

    def limpiarCli():
        try:
            var.ui.lineEdit_dni.setText('')
            var.ui.lineEdit_nombre.setText('')
            var.ui.lineEdit_fecha.setText('')
            var.ui.lineEdit_apellido.setText('')
            var.ui.lineEdit_direccion.setText('')
            var.ui.label_codigo.setText('')
            var.ui.lblstatus.setText('')
            var.ui.label_dni_valid.setText('')

            var.ui.spinBoxEnvio.setValue(0)
            Clientes.limpiarSexo()
            Clientes.limpiarPago()
            Clientes.limpiarProv()
        except Exception as error:
            print('Error: %s ' % str(error))

    def limpiarCliNoEstado():
        try:
            var.ui.lineEdit_dni.setText('')
            var.ui.lineEdit_nombre.setText('')
            var.ui.lineEdit_fecha.setText('')
            var.ui.lineEdit_apellido.setText('')
            var.ui.lineEdit_direccion.setText('')
            var.ui.label_codigo.setText('')
            var.ui.label_dni_valid.setText('')

            var.ui.spinBoxEnvio.setValue(0)
            Clientes.limpiarSexo()
            Clientes.limpiarPago()
            Clientes.limpiarProv()
        except Exception as error:
            print('Error: %s ' % str(error))

    def limpiarSexo():
        try:
            var.ui.rbtGroupSex.setExclusive(False)
            var.ui.rbtFem.setChecked(False)
            var.ui.rbtMas.setChecked(False)
            var.ui.rbtGroupSex.setExclusive(True)
        except Exception as error:
            print('Error limpiando los radiobutton sexo:', error)

    def limpiarPago():
        try:
            var.ui.chkEfectivo.setCheckState(QtCore.Qt.Unchecked)
            var.ui.chkTarjeta.setCheckState(QtCore.Qt.Unchecked)
            var.ui.chkTransferencia.setCheckState(QtCore.Qt.Unchecked)
        except Exception as error:
            print('Error: %s' % str(error))

    def limpiarProv():
        try:
            var.ui.cmbProv.setCurrentIndex(0)
        except Exception as error:
            print('Error limpiando el combobox provincia:', error)

    def buscarCliente():
        try:
            if (var.ui.lineEdit_dni.text().strip() != ''):
                dni = var.ui.lineEdit_dni.text()
                conexion.Conexion.buscarCli(dni)
            else:
                var.ui.lblstatus.setText('Error al Buscar! El campo de texto "DNI" no puede estar vacío.')
        except Exception as error:
            print('Error buscando clientes: %s' % str(error))

    def selEnvioLabel(self):
        try:
            valor = var.ui.spinBoxEnvio.value()
            if valor == 0:
                var.ui.label_envio_valor.setText('Recogida por cliente')
            elif valor == 1:
                var.ui.label_envio_valor.setText('Envío nacional paquetería exprés urgente')
            elif valor == 2:
                var.ui.label_envio_valor.setText('Envío nacional paquetería normal')
            elif valor == 3:
                var.ui.label_envio_valor.setText('Envío internacional')
        except Exception as error:
            print('Error en módulo seleccionar envío:', error)
