from listaHorizontalMatriz import listaHorizontal
class nodoLateral():
    def __init__(self, y):
        self.y = y
        self.siguiente = None
        self.anterior = None
        self.fila = listaHorizontal()
