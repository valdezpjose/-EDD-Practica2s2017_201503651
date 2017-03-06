from nodoPila import nodo

class pila():
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def agregarUltimo(self,dato):
        if self.vacia()== True:
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)

    def sacar(self):
        self.actual = None
        self.anterior = None
        self.actual = self.primero
        self.anterior = None
        info = self.ultimo.dato
        while (self.actual!= None):
            if (self.actual == self.ultimo):
                self.anterior.siguiente = None
                self.ultimo = self.anterior
            self.anterior = self.actual
            self.actual = self.actual.siguiente
        pass
        return info

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def reporte(self):
        aux = self.primero
        archivo = open("Pila.txt", "w")
        archivo.write('digraph G\n')
        archivo.write('{\n')
        while (aux != None):
            archivo.write(aux.dato+';\n')
            aux = aux.siguiente
        aux = self.primero
        while (aux.siguiente != None):
            archivo.write(aux.dato+'->'+aux.siguiente.dato+';\n')
            aux = aux.siguiente
        archivo.write('}\n')
        archivo.close()
