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

    def find(self, termo):
        k=0
        atual = self.raiz
        while k < len(termo):
            if atual is None: return None
            if k == len(termo) -1 and atual is None:
                return None
            elif k == len(termo) -1 and atual is not None:
                return atual.valor
            elif termo[k].lower() == atual.chave.lower():
                atual = atual.mid
                k += 1
            elif termo[k].lower() > atual.chave.lower():
                atual = atual.rig
            else:
                atual = atual.lef

        if atual is None: return None
        return atual.valor

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


def getAll(trie, no):
    if no is None: return []
    if no.valor is not None:
        return getAll(trie, no.lef) + getAll(trie, no.mid) + getAll(trie, no.rig) + [no.valor]
    if no.valor is None:
        return getAll(trie, no.lef) + getAll(trie, no.mid) + getAll(trie, no.rig)
    
    
