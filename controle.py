from palavra import *
from lista import Lista


class Controle:
    def __init__(self):
        self.numeroTermos = 0
        self.termos = list()
        self.dadosCarregados = True
    
    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False
    
    #TODO: implemente
    def __firstIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1        
        pos = -1
        #TODO: seu codigo aqui                 
        return pos
    
    #TODO: implemente
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1        
        pos = -1
        
        #TODO: seu codigo aqui
                 
        return pos
     
    #TODO: implemente   
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()
            
        #TODO: seu codigo aqui
            
        file = open(filename)
        linhas = file.readlines()
        for linha in linhas[1:]:
            n=0
            while linha[n] == ' ':
                n += 1
            self.termos.append(linha[n:len(linha]-1])
        
        self.termos.sort()
        self.dadosCarregados = True
    
    #TODO: implemente    
    def find(self, prefixo, qtd):
        pass
