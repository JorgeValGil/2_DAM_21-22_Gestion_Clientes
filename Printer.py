import os
from datetime import datetime

from PyQt5 import QtSql
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

import var


class Printer:

    def reportCli():
        try:
            var.rep = canvas.Canvas('informes/listadoclientes.pdf', pagesize=A4)
            Printer.cabecera()
            Printer.listadoclientes()
            query = QtSql.QSqlQuery()
            query.prepare('select codigo, dni, apellidos, nombre, fechalta from clientes order by apellidos, nombre')
            var.rep.setFont('Helvetica', size=10)
            if query.exec_():
                i = 50
                j = 690
                while query.next():
                    var.rep.drawString(i, j, str(query.value(0)))
                    var.rep.drawString(i + 40, j, str(query.value(1)))
                    var.rep.drawString(i + 130, j, str(query.value(2)))
                    var.rep.drawString(i + 280, j, str(query.value(3)))
                    var.rep.drawString(i + 420, j, str(query.value(4)))
                    if j - 30 < 50:
                        j = 690
                        Printer.pie()
                        var.rep.showPage()
                        Printer.cabecera()
                        Printer.listadoclientes()
                    else:
                        j = j - 30
            Printer.pie()
            var.rep.save()
            rootPath = ".\\informes"
            cont = 0
            for file in os.listdir(rootPath):
                if file.endswith('.pdf'):
                    os.startfile("%s/%s" % (rootPath, file))
                cont = cont + 1

        except Exception as error:
            print('Error reporcli %s' % str(error))

    def cabecera():
        try:
            logo = '.\\img\informe-usuarios.png'
            var.rep.setTitle('INFORMES')
            var.rep.setFont('Helvetica', size=10)
            var.rep.line(45, 820, 525, 820)
            var.rep.line(45, 745, 525, 745)
            var.rep.drawString(50, 805, 'INFORMES')
            var.rep.drawImage(logo, 450, 752)
        except Exception as error:
            print('Error cabecera %s' % str(error))

    def pie():
        try:
            var.rep.line(50, 50, 525, 50)
            fecha = datetime.today()
            fecha = fecha.strftime('%d.%m.%Y %H.%M.%S')
            var.rep.setFont('Helvetica-Oblique', size=7)
            var.rep.drawString(460, 40, str(fecha))
            var.rep.drawString(275, 40, str('Página %s' % var.rep.getPageNumber()))
        except Exception as error:
            print('Error cabecera %s' % str(error))

    def listadoclientes():
        try:
            var.rep.setFont('Helvetica-Bold', size=9)
            textlistado = 'LISTADO DE CLIENTES'
            var.rep.drawString(255, 735, textlistado)
            var.rep.line(45, 730, 525, 730)
            itemcli = ['ID', 'DNI', 'Apellidos', 'Nombre', 'Fecha Alta']
            var.rep.drawString(50, 710, itemcli[0])
            var.rep.drawString(90, 710, itemcli[1])
            var.rep.drawString(180, 710, itemcli[2])
            var.rep.drawString(325, 710, itemcli[3])
            var.rep.drawString(465, 710, itemcli[4])
            var.rep.line(45, 703, 525, 703)

        except Exception as error:
            print('Error cabecera %s' % str(error))
