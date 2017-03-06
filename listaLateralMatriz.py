from nodoLateralMatriz import nodoLateral
class listaLateral():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def insertar(self, inserta):
        if (self.primero==None):
                self.primero = inserta
                self.ultimo = inserta
        else:
            if (self.primero==self.ultimo):
                self.ultimo.siguiente = inserta
                inserta.anterior = self.ultimo
                self.ultimo = self.ultimo.siguiente
            else:
                self.temporal2 = None
                self.temporal1 = self.primero
                while (self.temporal1.y != self.ultimo.y):
                    self.temporal1 = self.temporal1.siguiente
                    pass
                self.temporal2 = self.temporal1.anterior
                self.temporal2.siguiente = inserta
                self.temporal1.anterior = inserta
                inserta.siguiente = self.temporal1
                inserta.anterior = self.temporal2

    def busqueda(self, posX):
        self.auxiliar = self.primero
        while (self.auxiliar.y != posX):
            self.auxiliar = self.auxiliar.siguiente
        return self.auxiliar

    def mostrarLista(self):
        self.temporal = self.primero
        while (self.temporal != None):
            print(self.temporal.y)
            self.temporal = self.temporal.siguiente

    def existeLateral(self, y):
        variableControl = False
        if (self.primero == None):
            variableControl = False
        else:
            temp = self.primero
            while (temp != None):
                if (temp.y == y):
                    variableControl = True
                else:
                    variableControl = False
                temp = temp.siguiente
        return variableControl
