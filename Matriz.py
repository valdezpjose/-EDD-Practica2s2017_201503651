from nodoMatriz import nodo
from nodoCabeceraMatriz import nodoCabecera
from nodoLateralMatriz import nodoLateral
from nodoProfunidadMatriz import nodoProfunidad
from listaCabeceraMatriz import listaCabecera
from listaLateralMatriz import listaLateral
from listaProfundidad import listaProf
class matriz():
    def __init__(self):
        self.cabecera = listaCabecera()
        self.lateral = listaLateral()
        self.profundidar = listaProf()

    def insertarNodo(self, x, y, dato):
        probar = matriz()
        self.contadorZ = 0
        self.nodoInsertar = nodo(dato,x,y,self.contadorZ)
        while (probar.existeDato(x,y,self.contadorZ) == True):
            self.contadorZ = self.contadorZ+1
            pass
        if (self.profundidar.existeProf(self.contadorZ) == False):
            self.profundidar.insertar(nodoProfunidad(self.contadorZ))
        if (self.profundidar.busquedaProf(self.contadorZ).cab.existeCabecera(x) == False):
            self.profundidar.busquedaProf(self.contadorZ).cab.insertar(nodoCabecera(x))
        if (self.profundidar.busquedaProf(self.contadorZ).lat.existeLateral(y) == False):
            self.profundidar.busquedaProf(self.contadorZ).lat.insertar(nodoLateral(y))

        zTemporal = self.profundidar.busquedaProf(self.contadorZ)
        cTemporal = zTemporal.cab.busqueda(x)
        lTemporal = zTemporal.lat.busqueda(y)

        cTemporal.columna.insertar(self.nodoInsertar)
        lTemporal.fila.insertar(self.nodoInsertar)



    def existeDato(self,x,y,z):
        valor = False
        if self.profundidar.primero == None:
            return valor
        if(self.profundidar.busquedaProf(z).cab.existeCabecera(x) == True):
            if(self.profundidar.busquedaProf(z).lat.existeLateral(y) == True):
                valor = True
                return valor
        return valor

    def busquedaPalabra(self,x,y,z):
        self.palabra = self.profundidar.busquedaProf(z).lat.busqueda(y).fila.busquedaHorizontal(x).dato
        return self.palabra

    def eliminarPalabra(self,x,y,dato):
        self.contadorZ = 0
        while (self.profundidar.existeProf(self.contadorZ) == True):
            if(self.profundidar.busquedaProf(self.contadorZ).cab.existeCabecera(x) == True):
                if(self.profundidar.busquedaProf(self.contadorZ).lat.existeLateral(y) == True):
                    if (self.profundidar.busquedaProf(self.contadorZ).lat.busqueda(y).fila.busquedaHorizontal(x).dato == dato):
                        self.profundidar.busquedaProf(self.contadorZ).lat.busqueda(y).fila.busquedaHorizontal(x).dato = ""
            contadorZ = contadorZ +1

    def listaDominio(self, dominio):
        resultado = ""
        contador = 0
        lis = self.profundidar.primero
        while (lis != None):
            aux = lis.cab.primero
            while (aux != None):
                if (aux.x == dominio):
                    resultado = resultado + aux.columna.mostrarLista() +","
                    pass
                aux = aux.siguiente
                pass
            lis =lis.siguiente
            contador = contador +1
            pass
        return resultado

    def listaPalabra(self, palabra):
        resultado = ""
        contador = 0
        lis = self.profundidar.primero
        while (lis != None):
            aux = lis.lat.primero
            while (aux != None):
                if (aux.y == palabra):
                    resultado = resultado + aux.fila.mostrarLista() + ","
                    pass
                aux = aux.siguiente
                pass
            lis =lis.siguiente
            contador = contador +1
            pass
        return resultado

    def reporte(self):
        archivo = open("Matriz.txt", "w")
        archivo.write('digraph G\n')
        archivo.write('{\n')
        self.contadorZ = 0
        while (self.profundidar.existeProf(self.contadorZ) == True):
            archivo.write(str(self.profundidar.busquedaProf(self.contadorZ).z)+';\n')
            nodoAuxiliar = self.profundidar.busquedaProf(self.contadorZ).cab.primero
            while (nodoAuxiliar != None):
                nodoAuxiliarTemporal = nodoAuxiliar.columna.primero
                while (nodoAuxiliarTemporal != None):
                    archivo.write(nodoAuxiliarTemporal.y +nodoAuxiliarTemporal.x +';\n')
                    nodoAuxiliarTemporal = nodoAuxiliarTemporal.abajo
                    pass
                nodoAuxiliar = nodoAuxiliar.siguiente
                pass
            nodoAuxiliar = self.profundidar.busquedaProf(self.contadorZ).cab.primero
            while (nodoAuxiliar != None):
                nodoAuxiliarTemporal = nodoAuxiliar.columna.primero
                while (nodoAuxiliarTemporal.abajo != None):
                    archivo.write(nodoAuxiliarTemporal.y + nodoAuxiliarTemporal.x+'->'+nodoAuxiliarTemporal.abajo.y +nodoAuxiliarTemporal.abajo.x+';\n')
                    archivo.write(nodoAuxiliarTemporal.abajo.y +nodoAuxiliarTemporal.abajo.x+'->'+nodoAuxiliarTemporal.y + nodoAuxiliarTemporal.x+';\n')
                    nodoAuxiliarTemporal = nodoAuxiliarTemporal.abajo
                    pass
                nodoAuxiliar = nodoAuxiliar.siguiente
                pass
            nodoAuxiliar = self.profundidar.busquedaProf(self.contadorZ).lat.primero
            while (nodoAuxiliar != None):
                nodoAuxiliarTemporal = nodoAuxiliar.fila.primero
                while (nodoAuxiliarTemporal.derecha != None):
                    archivo.write(nodoAuxiliarTemporal.y + nodoAuxiliarTemporal.x+'->'+nodoAuxiliarTemporal.derecha.y + nodoAuxiliarTemporal.derecha.x+';\n')
                    archivo.write(nodoAuxiliarTemporal.derecha.y + nodoAuxiliarTemporal.derecha.x+'->'+nodoAuxiliarTemporal.y + nodoAuxiliarTemporal.x+';\n')
                    nodoAuxiliarTemporal = nodoAuxiliarTemporal.derecha
                    pass
                nodoAuxiliar = nodoAuxiliar.siguiente
                pass
            if (self.profundidar.existeProf(self.contadorZ +1)) == True:
                archivo.write(str(self.profundidar.busquedaProf(self.contadorZ).z)+'->'+ str(self.profundidar.busquedaProf(self.contadorZ +1).z)+';\n')
                archivo.write(str(self.profundidar.busquedaProf(self.contadorZ +1).z)+'->'+ str(self.profundidar.busquedaProf(self.contadorZ).z)+';\n')
                pass
            self.contadorZ = self.contadorZ + 1
            pass
        archivo.write('}\n')
        archivo.close()
