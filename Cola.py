from nodoCola import nodo

class cola():
    def __init__(self):
        self.primero = None
        self.ultimo = None
    def vacia(self):
        return self.primero == None
    def insertar(self,dato):
        if self.vacia()== True:
            self.primero = self.ultimo = nodo(dato)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = nodo(dato)

    def sacar(self):
        info = self.primero.dato
        self.primero = self.primero.siguiente
        return info

    def recorrido(self):
        aux = self.primero
        while (aux != None):
            print(aux.dato)
            aux = aux.siguiente
    def reporte(self):
        aux = self.primero
        archivo = open("Cola.txt", "w")
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
