# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../../../if672_algoritmos/2016-2/autocomplete/src/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtWidgets


class Ui_MainWindow(object):        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.fileLabel = QtWidgets.QLabel(self.centralWidget)
        self.fileLabel.setGeometry(QtCore.QRect(10, 10, 59, 16))
        self.fileLabel.setObjectName("fileLabel")
        self.palavraLabel = QtWidgets.QLabel(self.centralWidget)
        self.palavraLabel.setGeometry(QtCore.QRect(10, 50, 59, 16))
        self.palavraLabel.setObjectName("palavraLabel")
        self.inputFileText = QtWidgets.QLineEdit(self.centralWidget)
        self.inputFileText.setGeometry(QtCore.QRect(70, 10, 181, 21))
        self.inputFileText.setObjectName("inputFileText")
        self.palavraText = QtWidgets.QLineEdit(self.centralWidget)
        self.palavraText.setEnabled(False)
        self.palavraText.setGeometry(QtCore.QRect(70, 50, 181, 21))
        self.palavraText.setObjectName("palavraText")
        self.outputText = QtWidgets.QTextEdit(self.centralWidget)
        self.outputText.setGeometry(QtCore.QRect(10, 100, 371, 131))
        self.outputText.setObjectName("outputText")
        self.resultadoLabel = QtWidgets.QLabel(self.centralWidget)
        self.resultadoLabel.setGeometry(QtCore.QRect(10, 80, 129, 16))
        self.resultadoLabel.setObjectName("resultadoLabel")
        self.botaoOK = QtWidgets.QPushButton(self.centralWidget)
        self.botaoOK.setEnabled(False)
        self.botaoOK.setGeometry(QtCore.QRect(260, 0, 51, 41))
        self.botaoOK.setObjectName("botaoOK")

        self.qtdPalavraLabel = QtWidgets.QLabel(self.centralWidget)
        self.qtdPalavraLabel.setGeometry(QtCore.QRect(260, 50, 31, 16))
        self.qtdPalavraLabel.setObjectName("qtdPalavraLabel")

        self.qtdPalavraText = QtWidgets.QLineEdit(self.centralWidget)
        self.qtdPalavraText.setGeometry(QtCore.QRect(290, 50, 41, 21))
        self.qtdPalavraText.setObjectName("qtdPalavraText")

        #RADIO BUTTON: Lista  ------------
        self.listaLabel = QtWidgets.QLabel(self.centralWidget)
        self.listaLabel.setGeometry(QtCore.QRect(260, 73, 51, 26))
        self.listaLabel.setObjectName("listaLabel")

        self.listaRadio = QtWidgets.QRadioButton(self.centralWidget)
        #JÁ DEIXA MARCADA/CHECADO
        self.listaRadio.toggled.connect(lambda: self.btnstate(self.listaRadio))
        self.listaRadio.setGeometry(QtCore.QRect(295,67,51,36))
        self.listaRadio.setObjectName("listaRadio")
        # --------------------------------

        #RADIO BUTTON: Tree  --------------
        self.treeLabel = QtWidgets.QLabel(self.centralWidget)
        self.treeLabel.setGeometry(QtCore.QRect(320, 73, 51, 26))
        self.treeLabel.setObjectName("treeLabel")

        self.arvoreRadio = QtWidgets.QRadioButton(self.centralWidget)
        self.arvoreRadio.toggled.connect(lambda: self.btnstate(self.arvoreRadio))
        self.arvoreRadio.setGeometry(QtCore.QRect(351,67,51,36))
        self.arvoreRadio.setObjectName("arvoreRadio")
        # --------------------------------

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Autocompletar"))
        self.fileLabel.setText(_translate("MainWindow", "Arquivo:"))
        self.palavraLabel.setText(_translate("MainWindow", "Palavra:"))
        self.resultadoLabel.setText(_translate("MainWindow", "Resultado:"))
        self.botaoOK.setText(_translate("MainWindow", "OK"))
        self.qtdPalavraLabel.setText(_translate("MainWindow", "Qtd:"))
        self.qtdPalavraText.setText(_translate("MainWindow", "5"))

        #ESCREVE OS LABELS NA TELA
        self.listaLabel.setText(_translate("MainWindow", "Lista:"))
        self.treeLabel.setText(_translate("MainWindow", "Trie:"))

        #VERIFICA QUAL RÁDIO ESTÁ ATIVO
        if self.listaRadio.isChecked() == True:
            self.resultadoLabel.setText("Resultado Lista:")
        else:
            self.resultadoLabel.setText("Resultado Trie:")


    def btnstate(self, b):

        if b.objectName()  == "listaRadio":
            if b.isChecked() == True:
                self.resultadoLabel.setText("Resultado Lista:")
                self.arvoreRadio.setChecked(False)

        if b.objectName() == "arvoreRadio":
            if b.isChecked() == True:
                self.resultadoLabel.setText("Resultado Trie:")
                self.listaRadio.setChecked(False)

