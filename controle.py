from palavra import *
from lista import Lista

def sortPesos(lista):
    if lista = []: return []
    else:
        pivo = lista.pop()
        return sortPesos([x for x in lista if x.peso <= pivo.peso]) + [pivo] + sortPesos([y for y in lista if y.peso > pivo.peso])
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
        while inicio < fim:
            meio = (inicio + fim)//2
            if self.termos[meio].termo.lower().startswith(prefixo.lower()):
                fim = meio
                pos = meio
            elif self.termos[meio].termo.lower() < prefixo.lower():
                inicio = meio
            elif self.termos[meio].termo.lower() > prefixo.lower():
                fim = meio
        #TODO: seu codigo aqui                 
        return pos
    
    #TODO: implemente
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos-1        
        pos = -1
        while inicio < fim:
            meio = (inicio + fim)//2
            if self.termos[meio].termo.lower().startswith(prefixo.lower()):
                inicio = meio
                pos = meio
            elif self.termos[meio].termo.lower() < prefixo.lower():
                inicio = meio
            elif self.termos[meio].termo.lower() > prefixo.lower():
                fim = meio
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
            self.termos.append(Palavra(linha[i+1:len(linha)-1], int(linha[n:i])))
        self.numeroTermos = int(linhas[0])

        file.close()
        self.termos.sort()
        self.dadosCarregados = True

    #TODO: implemente    
    def find(self, prefixo, qtd):
        '''
        tamanho = len(prefixo)
        sugestoes = Lista()
        sugestaux = list()
        for termo in self.termos:
            if termo[0][:tamanho].lower() == prefixo.lower(): #usar first e last index of, compara por peso
                sugestaux.append((termo[1], termo[0]))
            if termo[0][:tamanho] > prefixo:
                break

        sugestaux.sort(reverse = True)
        '''
        sugestoes = Lista()
        inicio = self.__firstIndexOf(prefixo)
        fim = self.__lastIndexOf(prefixo) +1
        sugestaux = self.termos[inicio:fim]
        sugestaux = sortPesos(sugestaux)
            

        for resultado in sugestaux:
            if qtd == 0: break
            sugestoes.inserirOrdenado(resultado.termo)
            qtd -= 1
        
        return sugestoes
