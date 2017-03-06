from nodoProfunidadMatriz import nodoProfunidad
class listaProf():
    def __init__(self):
        self.primero = None
        self.ultimo = None
        self.auxiliar = None

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
                while (self.temporal1.z != self.ultimo.z):
                    self.temporal1 = self.temporal1.siguiente
                    pass
                self.temporal2 = self.temporal1.anterior
                self.temporal2.siguiente = inserta
                self.temporal1.anterior = inserta
                inserta.siguiente = self.temporal1
                inserta.anterior = self.temporal2

    def busquedaProf(self, posX):
        self.auxiliar = self.primero
        while (self.auxiliar.z != posX):
            self.auxiliar = self.auxiliar.siguiente
        return self.auxiliar

    def mostrarLista(self):
        self.temporal = self.primero
        while (self.temporal != None):
            print(self.temporal.z)
            self.temporal = self.temporal.siguiente

    def existeProf(self, z):
        variableControl = False
        if (self.primero == None):
            variableControl = False
        else:
            temp = self.primero
            while (temp != None):
                if (temp.z == z):
                    variableControl = True
                else:
                    variableControl = False
                temp = temp.siguiente
        return variableControl
