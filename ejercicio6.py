class Datopolinomio(object):
    
    def __init__ (self, valor, termino):
        self.valor = valor
        self.termino = termino
        
class Polinomio(object):
    
    def __init__ (self):
        self.termino_mayor = None
        self.grado = -1
        
    def agregar_termino(polinomio, termino, valor):
        aux = Nodo()