class Zoologico:
    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion
        self._zonas = []

    def cantidadTotalAnimales(self):
        cont = 0
        for i in range(len(self._zonas)):
            cont += self._zonas[i].cantidadAnimales()
        return cont
    
    def agregarZonas(self, zona):
        self._zonas.append(zona)

    def getNombre(self):
        return self._nombre
    
    def getUbicacion(self):
        return self._ubicacion
    
    def getZonas(self):
        return self._zonas
    
    def setNombre(self, nombre):
        self._nombre = nombre

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion
    

    