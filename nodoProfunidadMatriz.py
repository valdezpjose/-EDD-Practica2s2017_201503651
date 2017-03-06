from listaCabeceraMatriz import listaCabecera
from listaLateralMatriz import listaLateral
class nodoProfunidad():
    def __init__(self, z):
        self.z = z
        self.siguiente = None
        self.anterior = None
        self.cab = listaCabecera()
        self.lat = listaLateral()
