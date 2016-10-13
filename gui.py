from mainwindow import Ui_MainWindow
from controle import *

class GUI(Ui_MainWindow):
    def __init__(self):
        self.controle = Controle()

    def setupUi(self, MainWindow):
        Ui_MainWindow.setupUi(self, MainWindow)
        self.inputFileText.textChanged.connect(self.inputFileChanged)
        self.botaoOK.clicked.connect(self.carregarDados)
        self.qtdPalavraText.textChanged.connect(self.autocompletar)
        self.palavraText.textChanged.connect(self.autocompletar)

    def inputFileChanged(self):
        self.botaoOK.setEnabled(self.inputFileText.text().strip() != "")
    
    def carregarDados(self):
        if self.listaRadio.isChecked():
            self.controle = ImplementacaoLista()
        elif self.arvoreRadio.isChecked():
            self.controle = ImplementacaoTrie()
        self.controle.carregarDados(self.inputFileText.text())
        self.palavraText.setEnabled(True)
    
    def autocompletar(self):
        texto = self.palavraText.text()
        qtd = self.qtdPalavraText.text()
        if texto != "" and qtd != "":
            self.controle.start()
            lista = self.controle.find(texto,int(qtd))
            self.outputText.setText(str(lista))
            tempo = self.controle.stop()
            self.resultadoLabel.setText(tempo)
        else:
            self.outputText.clear()
