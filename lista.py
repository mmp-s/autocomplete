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
    def inserirOrdenado(self, item):    
        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''

        if self.vazia():
            self.ultimo.prox = No(item, self.primeiro, None)
            self.ultimo = self.ultimo.prox
            self.tamanho += 1
            pass

        atual = self.primeiro.prox

        while (atual.prox is not None) and (atual.item < item):
            aux = atual
            atual = aux.prox

        if atual.prox is None and (atual.item < item):
            atual.prox = No(item, atual, None)
            self.ultimo = atual.prox
            self.tamanho += 1

        elif atual.prox is not None and atual.item < item:
            aux = atual.prox
            elemento = No(item, atual, aux)
            aux.ant = elemento
            atual.prox = elemento
            self.tamanho += 1

        elif atual.item == item: atual.item = item

        else:
            aux = atual.ant
            elemento = No(item, aux, atual)
            aux.prox = elemento
            atual.ant = elemento
            self.tamanho += 1
        
        pass

    #TODO: implemente    
    def removerFim(self):
        if self.vazia(): return None
        ultimo = self.ultimo
        aux = ultimo.ant
        aux.prox = None
        ultimo.ant = None
        self.ultimo = aux
        del ultimo
        self.tamanho -= 1
        
        pass

    def find(self, item):
        if self.vazia(): return 'lista vazia'
        atual = self.primeiro.prox
        while atual is not None:
            if atual.item == item:
                return item
            atual = atual.prox
        if atual == None: return 'item nao esta na lista'
    
    #TODO: implemente        
    def __str__(self):
        if self.vazia():
            return "lista vazia"
        atual = self.primeiro.prox
        string = ''
        while atual is not None:
            if atual == self.ultimo:
                string += str(atual.item)
                break
            else:
                string += str(atual.item) + ' '
                atual = atual.prox
        return string
    
    def __repr__(self):
        return str(self)
