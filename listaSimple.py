from nodoLista import nodo

class lista():
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
    def borrarDato(self, num):
        contador = 0
        self.actual = None
        self.anterior = None
        self.actual = self.primero
        self.anterior = None
        while (self.actual!= None):
            if (contador == num):
                if (self.actual == self.primero):
                    self.primero = self.primero.siguiente
                else:
                    if (self.actual == self.ultimo):
                        self.anterior.siguiente = None

                    else:
                        self.anterior.siguiente = self.actual.siguiente
            contador = contador + 1
            self.anterior = self.actual
            self.actual = self.actual.siguiente
        pass
    def buscarPalabra(self, palabra):
        indice = 0
        posicion = 0
        validacion = False
        actual = self.primero
        if (self.primero.dato == palabra):
            return "Dato se encuentra en: 0"
        else:
            while actual != None:
                if (actual.dato == palabra):
                    validacion = True
                    posicion = indice
                actual = actual.siguiente
                indice = indice + 1
        if (validacion == True):
            return "Dato se encuentra en: "+str(posicion)
        else:
            return "No se encontro el dato"

    def recorrido(self):
        aux = self.primero
        while aux != None:
            print(aux.dato)
            aux = aux.siguiente

    def reporte(self):
        aux = self.primero
        archivo = open("listaSimple.txt", "w")
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
