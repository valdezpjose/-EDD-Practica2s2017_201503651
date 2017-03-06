from nodoMatriz import nodo
class listaHorizontal():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, inserta):
        if (self.primero==None):
                self.primero = inserta
                self.ultimo = inserta
        else:
            if (self.primero==self.ultimo):
                self.ultimo.derecha = inserta
                inserta.izquierda = self.ultimo
                self.ultimo = self.ultimo.derecha
            else:
                self.temporal2 = None
                self.temporal1 = self.primero
                while (self.temporal1.x != self.ultimo.x):
                    self.temporal1 = self.temporal1.derecha
                    pass
                self.temporal2 = self.temporal1.izquierda
                self.temporal2.derecha = inserta
                self.temporal1.izquierda = inserta
                inserta.derecha = self.temporal1
                inserta.izquierda = self.temporal2

    def busquedaHorizontal(self, posX):
        self.auxiliar = self.primero
        while (self.auxiliar.x != posX):
            self.auxiliar = self.auxiliar.derecha
        return self.auxiliar

    def mostrarLista(self):
        Palabras = ""
        self.temporal = self.primero
        while (self.temporal != None):
            print(self.temporal.dato)
            if (self.temporal.dato != ""):
                Palabras = Palabras + self.temporal.dato + ","
                pass
            self.temporal = self.temporal.derecha
        return Palabras
