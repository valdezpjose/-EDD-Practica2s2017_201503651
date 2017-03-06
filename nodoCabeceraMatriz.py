from listaVerticalMatriz import listaVertical
class nodoCabecera():
    def __init__(self, x):
        self.x = x
        self.siguiente = None
        self.anterior = None
        self.columna = listaVertical()
