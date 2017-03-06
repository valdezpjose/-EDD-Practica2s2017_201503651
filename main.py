from listaSimple import lista
from Cola import cola
from Pila import pila
from flask import Flask
from listaHorizontalMatriz import listaHorizontal
from listaVerticalMatriz import listaVertical
from nodoMatriz import nodo
from Matriz import matriz
from flask import Flask, request, Response
app = Flask("EDD_codigo_ejemplo")
c = cola()
p = pila()
l = lista()
m = matriz()
class Usuario():
    def __init__(self,prueba):
        self.prueba = prueba

@app.route('/queue',methods=['POST'])
def queue():
    c.insertar(str(request.form['dato']))
    print(c.recorrido())
    return "Ingresado"

@app.route('/dequeue',methods=['POST'])
def dequeue():
    prueba = str(request.form['dato'])
    return c.sacar()

@app.route('/push',methods=['POST'])
def push():
    p.agregarUltimo(str(request.form['dato']))
    print(p.recorrido())
    return "Ingresado"

@app.route('/pop',methods=['POST'])
def pop():
    prueba = str(request.form['dato'])
    return p.sacar()

@app.route('/ingresarLista',methods=['POST'])
def ingresarLista():
    l.agregarUltimo(str(request.form['dato']))
    print(p.recorrido())
    return "Ingresado"

@app.route('/borrarDatoLista',methods=['POST'])
def borrarDatoLista():
    l.borrarDato(int(str(request.form['dato'])))
    return "Dato Eliminado"

@app.route('/buscarPalabra',methods=['POST'])
def buscarPalabra():
    prueba = str(request.form['dato'])
    return l.buscarPalabra(prueba)

@app.route('/ingresarMatriz',methods=['POST'])
def ingresarMatriz():
    m.insertarNodo(str(request.form['x']),str(request.form['y']),str(request.form['dato']))
    return "Ingresado"

@app.route('/borrarMatriz',methods=['POST'])
def borrarMatriz():
    m.eliminarPalabra(str(request.form['x']),str(request.form['y']),str(request.form['dato']))
    return "Dato Eliminado"

@app.route('/buscarLetra',methods=['POST'])
def buscarLetra():
    prueba = str(request.form['dato'])
    return m.listaPalabra(prueba)

@app.route('/buscarDominio',methods=['POST'])
def buscarDominio():
    prueba = str(request.form['dato'])
    return m.listaDominio(prueba)

@app.route('/reporteCola',methods=['POST'])
def reporteCola():
    prueba = str(request.form['dato'])
    c.reporte()
    return "REPORTE COLA GENERADO"

@app.route('/reportePila',methods=['POST'])
def reportePila():
    prueba = str(request.form['dato'])
    p.reporte()
    return "REPORTE PILA GENERADO"

@app.route('/reporteLista',methods=['POST'])
def reporteLista():
    prueba = str(request.form['dato'])
    l.reporte()
    return "REPORTE LISTA GENERADO"


@app.route('/reporteMatriz',methods=['POST'])
def reporteMatriz():
    prueba = str(request.form['dato'])
    m.reporte()
    return "REPORTE MATRIZ GENERADO"




@app.route("/")
def hellof():
	return "WEB ACTIVO"

if __name__ == "__main__":
  app.run(debug=True)
