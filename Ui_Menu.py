# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Git\python\hab-a-sqlite\Menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 220)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_hab = QtWidgets.QPushButton(self.centralwidget)
        self.btn_hab.setGeometry(QtCore.QRect(30, 25, 93, 28))
        self.btn_hab.setObjectName("btn_hab")
        self.lbl_hab = QtWidgets.QLabel(self.centralwidget)
        self.lbl_hab.setGeometry(QtCore.QRect(130, 31, 450, 16))
        self.lbl_hab.setObjectName("lbl_hab")
        self.lbl_cant_registros = QtWidgets.QLabel(self.centralwidget)
        self.lbl_cant_registros.setGeometry(QtCore.QRect(160, 70, 100, 20))
        self.lbl_cant_registros.setText("")
        self.lbl_cant_registros.setObjectName("lbl_cant_registros")
        self.btn_base = QtWidgets.QPushButton(self.centralwidget)
        self.btn_base.setGeometry(QtCore.QRect(30, 140, 93, 28))
        self.btn_base.setObjectName("btn_base")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 72, 130, 16))
        self.label.setObjectName("label")
        self.txt_programa = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_programa.setGeometry(QtCore.QRect(130, 100, 220, 22))
        self.txt_programa.setObjectName("txt_programa")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(31, 103, 70, 16))
        self.label_2.setObjectName("label_2")
        self.btn_abrir_directorio = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrir_directorio.setGeometry(QtCore.QRect(140, 140, 160, 28))
        self.btn_abrir_directorio.setObjectName("btn_abrir_directorio")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ani"))
        self.btn_hab.setText(_translate("MainWindow", "Cargar .hab"))
        self.lbl_hab.setText(_translate("MainWindow", "Ubicación del archivo"))
        self.btn_base.setText(_translate("MainWindow", "Cargar a Base"))
        self.label.setText(_translate("MainWindow", "Cantidad de registros:"))
        self.label_2.setText(_translate("MainWindow", "Programa"))
        self.btn_abrir_directorio.setText(_translate("MainWindow", "Abrir ubicación del excel"))