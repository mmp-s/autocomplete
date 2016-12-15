class No:
    def __init__(self,chave=None,valor=None,lef=None,rig=None,mid=None):
        self.chave=chave
        self.valor=valor
        self.lef = lef
        self.rig = rig
        self.mid = mid

class Trie:
    def __init__ (self):
        self.raiz = No()
        self.valores = list()

    def vazia(self):
        return self.raiz.chave == None

    def inserir(self, palavra):
        k=0
        atual = self.raiz
        while k < len(palavra.termo):
            if self.vazia() and len(palavra.termo) > 1:
                atual.chave = palavra.termo[k]
                atual.mid = No()
                atual = atual.mid
                k += 1
            elif self.vazia() and len(palavra.termo) == 1:
                atual.chave = palavra.termo[k]
                atual.valor = palavra
            elif k == len(palavra.termo) -1 and atual.valor is None:
                atual.chave = palavra.termo[k]
                atual.valor = palavra
                k += 1
            elif k == len(palavra.termo) -1 and atual.valor is not None:
                atual.valor = palavra
                k += 1
            elif atual.chave is None:
                atual.chave = palavra.termo[k]
                atual.mid = No()
                atual = atual.mid
                k += 1
            elif palavra.termo[k].lower() == atual.chave.lower() and atual.mid is not None:
                atual = atual.mid
                k += 1
            elif palavra.termo[k].lower() == atual.chave.lower() and atual.mid is None:
                atual.mid = No()
                atual = atual.mid
                k += 1
            elif palavra.termo[k].lower() > atual.chave.lower() and atual.rig is None:
                atual.rig = No()
                atual = atual.rig
            elif palavra.termo[k].lower() < atual.chave.lower() and atual.lef is None:
                atual.lef = No()
                atual = atual.lef
            elif palavra.termo[k].lower() > atual.chave.lower() and atual.rig is not None:
                atual = atual.rig
            elif palavra.termo[k].lower() < atual.chave.lower() and atual.lef is not None:
                atual = atual.lef


def getPrefix(trie, no):
    if no is None: return []
    if no.valor is not None:
        return getPrefix(trie, no.lef) + getPrefix(trie, no.mid) + getPrefix(trie, no.rig) + [no.valor]
    if no.valor is None:
        return getPrefix(trie, no.lef) + getPrefix(trie, no.mid) + getPrefix(trie, no.rig)

def heapify(lista, n, i):
    largest = i
    left = (2 * i) + 1
    right = (2 * i) + 2
 
    if left < n and lista[i].peso > lista[left].peso:
        largest = left
 
    if right < n and lista[largest].peso > lista[right].peso:
        largest = right
 
    if largest != i:
        lista[i],lista[largest] = lista[largest],lista[i]
 
        heapify(lista, n, largest)
 
def heapSort(lista):
    n = len(lista)
    for i in range(n, -1, -1):
        heapify(lista, n, i)
 
    for i in range(n-1, 0, -1):
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
