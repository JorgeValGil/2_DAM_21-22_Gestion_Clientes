from PyQt5 import QtWidgets, QtSql
import var


class Conexion():
    def db_connect(filename):
        var.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        var.db.setDatabaseName(filename)
        if not var.db.open():
            QtWidgets.QMessageBox.critical(None, 'No se puede abrir la base de datos',
                                           'No se puede establecer la conexion.\n' 'Haz Click para Cancelar',
                                           QtWidgets.QMessageBox.Cancel)

            return False
        else:
            print('Conexión Establecida')
            return True

    def db_close():
        if var.db.close():
            print('Conexión con base de datos cerrada')
        else:
            print('Error al cerrar conexión base de datos cerrada')

    def cargarCli(cliente):
        print('cargar cliente')
        query = QtSql.QSqlQuery()
        query.prepare(
            'insert into clientes (dni, apellidos, nombre, fechalta, direccion, provincia, sexo, formaspago, '
            'formaenvio) VALUES (:dni, :apellidos, :nombre, :fechalta, :direccion, :provincia, :sexo, '
            ':formaspago, :formaenvio)')
        query.bindValue(':dni', str(cliente[0]))
        query.bindValue(':apellidos', str(cliente[1]))
        query.bindValue(':nombre', str(cliente[2]))
        query.bindValue(':fechalta', str(cliente[3]))
        query.bindValue(':direccion', str(cliente[4]))
        query.bindValue(':provincia', str(cliente[5]))
        query.bindValue(':sexo', str(cliente[6]))
        # pagos = ' '.join(cliente[7]) si queremos un texto, pero nos viene mejor meterlo como una lista
        query.bindValue(':formaspago', str(cliente[7]))
        query.bindValue(':formaenvio', str(cliente[8]))
        # print(pagos)
        if query.exec_():
            print('Inserción correcta')
            var.ui.lblstatus.setText('Cliente con dni ' + str(cliente[0]) + ' creado')
            Conexion.mostrarClientes()
        else:
            print('Error: ', query.lastError().text())

    def mostrarClientes():
        var.ui.tableClientes.clearContents()
        index = 0
        query = QtSql.QSqlQuery()
        query.prepare('select dni, apellidos, nombre from clientes')
        if query.exec_():
            while query.next():
                dni = query.value(0)
                apellidos = query.value(1)
                nombre = query.value(2)
                var.ui.tableClientes.setRowCount(index + 1)  # crea la fila y a continuacion mete los datos
                var.ui.tableClientes.setItem(index, 0, QtWidgets.QTableWidgetItem(dni))
                var.ui.tableClientes.setItem(index, 1, QtWidgets.QTableWidgetItem(apellidos))
                var.ui.tableClientes.setItem(index, 2, QtWidgets.QTableWidgetItem(nombre))
                index += 1
        else:
            print("Error mostrar clientes: ", query.lastError().text())

    def buscarCli(dni):
        query = QtSql.QSqlQuery()
        query.prepare(
            'select codigo, dni, apellidos, nombre, fechalta, direccion, provincia, sexo, '
            'formaspago, formaenvio from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                codigo = query.value(0)
                codigo_str = str(codigo)
                dni_query = query.value(1)
                apellidos = query.value(2)
                nombre = query.value(3)
                fechalta = query.value(4)
                direccion = query.value(5)
                provincia = query.value(6)
                sexo = query.value(7)
                formaspago = query.value(8)
                formaenvio = query.value(9)

                var.ui.label_codigo.setText(codigo_str)
                var.ui.lineEdit_apellido.setText(apellidos)
                var.ui.lineEdit_nombre.setText(nombre)
                var.ui.lineEdit_direccion.setText(direccion)
                var.ui.lineEdit_fecha.setText(fechalta)

                indice_provincia = var.datosprovincias.index(provincia)
                var.ui.cmbProv.setCurrentIndex(indice_provincia)

                var.ui.spinBoxEnvio.setValue(int(formaenvio))

                if sexo == 'Hombre':
                    var.ui.rbtMas.setChecked(True)
                if sexo == 'Mujer':
                    var.ui.rbtFem.setChecked(True)

                var.ui.chkEfectivo.setChecked(False)
                var.ui.chkTarjeta.setChecked(False)
                var.ui.chkTransferencia.setChecked(False)

                if 'Efectivo' in formaspago:
                    var.ui.chkEfectivo.setChecked(True)
                if 'Tarjeta' in formaspago:
                    var.ui.chkTarjeta.setChecked(True)
                if 'Transferencia' in formaspago:
                    var.ui.chkTransferencia.setChecked(True)

                var.ui.lblstatus.setText('Cliente con dni ' + query.value(1) + ' cargado')
        else:
            print('Error buscando clientes: ', query.lastError().text())

    def bajaCli(dni):
        print('dni', dni)
        query = QtSql.QSqlQuery()
        query.prepare('delete from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            if query.numRowsAffected() > 0:
                print('Baja cliente')
                var.ui.lblstatus.setText('Cliente con dni ' + dni + ' dado de baja')
            else:
                var.ui.lblstatus.setText('No se ha borrado ningún cliente con el dni ' + dni)
        else:
            print('Error mostrar clientes: ', query.lastError().text())

    def modifCli(codigo, newdata):
        query = QtSql.QSqlQuery()
        query.prepare(
            'update clientes set dni=:dni, apellidos=:apellidos, nombre=:nombre, fechalta=:fechalta, '
            'direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, '
            'formaenvio=:formaenvio where codigo=:codigo')
        query.bindValue(':codigo', int(codigo))
        query.bindValue(':dni', str(newdata[0]))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':fechalta', str(newdata[3]))
        query.bindValue(':direccion', str(newdata[4]))
        query.bindValue(':provincia', str(newdata[5]))
        query.bindValue(':sexo', str(newdata[6]))
        query.bindValue(':formaspago', str(newdata[7]))
        query.bindValue(':formaenvio', str(newdata[8]))

        if query.exec_():
            print('Cliente modificado')
            var.ui.lblstatus.setText('Cliente con dni ' + str(newdata[0]) + ' modificado')
        else:
            print("Error modificar cliente: ", query.lastError().text())

    def buscarCliExcel(dni):
        cliente_exists = False
        query = QtSql.QSqlQuery()
        query.prepare('select * from clientes where dni = :dni')
        query.bindValue(':dni', dni)
        if query.exec_():
            while query.next():
                cliente_exists = True
        else:
            print('Error buscando clientes: ', query.lastError().text())

        return cliente_exists

    def modifCliExcel(newdata):
        query = QtSql.QSqlQuery()
        query.prepare(
            'update clientes set apellidos=:apellidos, nombre=:nombre, fechalta=:fechalta, '
            'direccion=:direccion, provincia=:provincia, sexo=:sexo, formaspago=:formaspago, '
            'formaenvio=:formaenvio where dni=:dni')
        query.bindValue(':dni', str(newdata[0]))
        query.bindValue(':apellidos', str(newdata[1]))
        query.bindValue(':nombre', str(newdata[2]))
        query.bindValue(':fechalta', str(newdata[3]))
        query.bindValue(':direccion', str(newdata[4]))
        query.bindValue(':provincia', str(newdata[5]))
        query.bindValue(':sexo', str(newdata[6]))
        query.bindValue(':formaspago', str(newdata[7]))
        query.bindValue(':formaenvio', str(newdata[8]))

        if query.exec_():
            print('Cliente con dni ' + str(newdata[0]) + ' modificado desde Excel')
        else:
            print("Error modificar cliente desde Excel: ", query.lastError().text())
