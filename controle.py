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
            i = n
            while linha[i] != '\t':
                i += 1
            termos = Palavra(linha[i+1:len(linha)-1], int(linha[n:i]))
            self.termos.append((termos.termo, termos.peso))
            self.numeroTermos += 1
        
        self.termos.sort()
        self.dadosCarregados = True

    def buscaBinaria(elemento, lista):
        if lista == [] : return None
        elif len(lista) == 1 and elemento == lista[0]: return elemento
        else: return None    
        pivo = lista[len(lista)//2]
        if pivo == elemento: return elemento
        elif pivo > elemento: return buscaBinaria(elemento, lista[:len(lista)//2])
        else: return buscaBinaria(elemento, lista[len(lista)//2:])
        
    #TODO: implemente    
    def find(self, prefixo, qtd):
        meio = self.numeroTermos // 2
        tamanho = len(prefixo)
        sugestoes = list()
        for termo in self.termos:
            if termo[0][:tamanho].lower() == prefixo.lower():
                sugestoes.append(termo)
            if termo[0][:tamanho] > prefixo:
                break
        return sugestoes
