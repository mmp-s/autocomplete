class Palavra:
    def __init__(self,termo="",peso=-1):
        self.termo = termo
        self.peso = peso

    def __lt__(self,other):
        if self.termo.lower() < other.termo.lower(): return True
        else: return False
        pass
    
    def __str__(self):
        return "{0}, {1}".format(self.termo,self.peso)
    
    def __repr__(self):
        return self.__str__()
      
def comparaPorPrefixo(palavra, prefixo):
    if palavra.termo.lower().startswith(prefixo.lower()): 
        return 0
    elif palavra.termo.lower() < prefixo.lower():
        return -1
    elif palavra.termo.lower() > prefixo.lower():
        return 1

def comparaPorPeso(palavra1, palavra2):
    if palavra1.peso < palavra2.peso:
        return -1
    elif palavra1.peso > palavra2.peso:
        return 1
    else: return 0
