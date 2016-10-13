from palavra import *
from lista import Lista
import sys
from time import perf_counter
import numpy
from trie import *
import datetime

def trocar(v, i, j):
    temp = v[i]
    v[i] = v[j]
    v[j] = temp

def particao(v, esq, dir):
    pivo = v[esq]; i = esq; j = dir+1
    while(True):
        i+=1
        while v[i].peso < pivo.peso:
            if i >= dir: break
            i+=1
        j-=1
        while v[j].peso > pivo.peso:
            if j <= esq: break
            j-=1
        if i >= j : break
        trocar(v,i,j)
    trocar(v,esq,j)
    return j

def qs (v, esq, dir):
    if esq >= dir: return
    p = particao(v,esq,dir)
    qs(v,esq,p-1)
    qs(v,p+1,dir)

def quicksort(v, N):
    qs(v, 0, N-1)
def sortPesos(lista):
    if lista == []: return []
    else:
        pivo = lista.pop()
        return sortPesos([y for y in lista if y.peso > pivo.peso]) + [pivo] + sortPesos([x for x in lista if x.peso <= pivo.peso])

class Controle:
    def __init__(self):
        self.__start = None
        self.__stop = None
    def start(self):
        self.__start = datetime.datetime.now()
    def stop(self):
        self.__stop = datetime.datetime.now()
        return str(self.__stop - self.__start)
    def find(self, prefixo, qtd): raise NotImplementedError("Selecione estrutura de dados")
    def carregarDados(self, filename): raise NotImplementedError("Selecione estrutura de dados")

class ImplementacaoLista(Controle):
    def __init__(self):
        Controle.__init__(self)
        self.numeroTermos = 0
        self.termos = list()
        self.dadosCarregados = True

    def __apagarTermos(self):
        self.termos = []
        self.numeroTermos = 0
        self.dadosCarregados = False
    
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
    
    def __lastIndexOf(self, prefixo):
        inicio = 0
        fim = self.numeroTermos        
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
       
    def carregarDados(self,filename):
        if self.dadosCarregados:
            self.__apagarTermos()
            
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
        
class ImplementacaoTrie(Controle):
    def __init__(self):
        Controle.__init__(self)
        self.trie = Trie()

    def carregarDados(self, filename):
        file = open(filename)
        linhas = file.readlines()
        for linha in linhas[1:]:
            n=0
            while linha[n] == ' ':
                n += 1
            i = n
            while linha[i] != '\t':
                i += 1
            self.trie.inserir(Palavra(linha[i+1:len(linha)-1], int(linha[n:i])))

        file.close()

    def find(self, prefixo, qtd):
        k=0
        atual = self.trie.raiz
        while k < len(prefixo):
            if atual is None: return ''
            if prefixo[k].lower() == atual.chave.lower():
                atual = atual.mid
                k += 1
            elif prefixo[k].lower() > atual.chave.lower():
                atual = atual.rig
            else:
                atual = atual.lef
        sugestoes = getAll(self.trie, atual)
        sugestoes = sortPesos(sugestoes)
        string = ''
        for x in sugestoes:  
            if qtd == 0: break
            if qtd == 1:
                string =string + x.termo
            else:
                string =string + x.termo + '\n'
            qtd -= 1 
        return string
