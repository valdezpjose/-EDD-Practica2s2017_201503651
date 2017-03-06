from nodoMatriz import nodo
class listaVertical():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, inserta):
        if (self.primero==None):
                self.primero = inserta
                self.ultimo = inserta
        else:
            if (self.primero==self.ultimo):
                self.ultimo.abajo = inserta
                inserta.arriba = self.ultimo
                self.ultimo = self.ultimo.abajo
            else:
                self.temporal2 = None
                self.temporal1 = self.primero
                while (self.temporal1.y != self.ultimo.y):
                    self.temporal1 = self.temporal1.abajo
                    pass
                self.temporal2 = self.temporal1.arriba
                self.temporal2.abajo = inserta
                self.temporal1.arriba = inserta
                inserta.abajo = self.temporal1
                inserta.arriba = self.temporal2

    def busquedaVertical(self, posY):
        self.auxiliar = self.primero
        while (self.auxiliar.y != posY):
            self.auxiliar = self.auxiliar.abajo
        return self.auxiliar

    def mostrarLista(self):
        Palabras = ""
        self.temporal = self.primero
        while (self.temporal != None):
            if (self.temporal.dato != ""):
                Palabras = Palabras + self.temporal.dato + ","
                pass
            self.temporal = self.temporal.abajo
        return Palabras
