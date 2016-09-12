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
    
    #TODO: implemente
    def inserirOrdenado(self, item, cmp):    
        '''
        Insere ordenado conforme funcao de comparacao passada como parametro.
        cmp: funcao de comparacao que retorna <0, 0 ou >0 se primeiro valor
            for menor, igual ou maior que o segundo valor 
        '''
        pass
    
    #TODO: implemente    
    def removerFim(self):
        pass
    
    #TODO: implemente        
    def __str__(self):
        return ""
    
    def __repr__(self):
        return str(self)