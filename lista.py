def cmp(atual, item):
    if item == atual:
        return '0'
    elif item < atual:
        return '<0'
    else:
        return '>0'

class No:
    def __init__(self,item=None,ant=None,prox=None):
        self.item = item
        self.ant = ant
        self.prox = prox
    
class Lista:

    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0
    
    def size(self):
        return self.tamanho

    def vazia(self):
        return self.primeiro == self.ultimo
    
    #TODO: implemente
    def inserirOrdenado(self, item, cmp):    
        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''
        atual = self.item

        if self.vazia():
            elemento = No()
            elemento.item = item
            self.ultimo.prox = elemento
            self.ultimo = elemento
            elemento.ant = self.primeiro

        elif cmp(atual, item) == '0': self.item = item

        elif cmp(atual, item) == '<0': inserirOrdenado(self.prox, item, cmp)

        else:
            elemento = No()
            elemento.item = item
            anterior = self.ant
            self.ant = elemento
            elemento.prox = self
            elemento.ant = anterior
            anterior.prox = elemento
        
        pass
    
    #TODO: implemente    
    def removerFim(self):
        pass
    
    #TODO: implemente        
    def __str__(self):
        return ""
    
    def __repr__(self):
        return str(self)
