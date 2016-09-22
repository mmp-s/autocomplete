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
        fim = self.numeroTermos
        pos = -1
        encontrado = False
        while not encontrado and inicio < fim:
            meio = (inicio + fim)// 2
            if comparaPorPrefixo(self.termos[meio], prefixo) == 0 and comparaPorPrefixo(self.termos[meio-1], prefixo) != 0:
                pos = meio
                encontrado = True
            elif comparaPorPrefixo(self.termos[meio], prefixo) == 0:
                fim = meio
            elif comparaPorPrefixo(self.termos[meio], prefixo) < 0:
                inicio = meio + 1
            elif comparaPorPrefixo(self.termos[meio], prefixo) > 0:
                fim = meio
        return pos
    
    #TODO: implemente
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1        
        pos = -1
        encontrado = False
        while not encontrado and inicio < fim:
            meio = (inicio + fim)// 2
            if comparaPorPrefixo(self.termos[meio], prefixo) == 0 and comparaPorPrefixo(self.termos[meio+1], prefixo) != 0:
                pos = meio
                encontrado = True
            elif comparaPorPrefixo(self.termos[meio], prefixo) == 0:
                inicio = meio +1
            elif comparaPorPrefixo(self.termos[meio], prefixo) < 0:
                inicio = meio +1
            elif comparaPorPrefixo(self.termos[meio], prefixo) > 0:
                fim = meio
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
            self.termos.append(Palavra(linha[i+1:len(linha)-1], int(linha[n:i])))
        self.numeroTermos = int(linhas[0])

        file.close()
        self.termos.sort()
        self.dadosCarregados = True

    #TODO: implemente    
    def find(self, prefixo, qtd):
        sugestoes = Lista()
        inicio = self.__firstIndexOf(prefixo)
        fim = self.__lastIndexOf(prefixo) +1
        for resultado in self.termos[inicio:fim]:
            if sugestoes.size() < qtd:
                sugestoes.inserirOrdenado(resultado, comparaPorPeso)
            elif sugestoes.size() == qtd and comparaPorPeso(sugestoes.ultimo.item, resultado) < 0:
                sugestoes.removerFim()
                sugestoes.inserirOrdenado(resultado, comparaPorPeso)
            else: continue
        
        return sugestoes
