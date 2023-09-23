from animal import Animal

class Pez(Animal):
    listado = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, cantidadAletas):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.cantidadAletas = cantidadAletas
        Animal.pez += 1
        Pez.listado.append(self)

    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return Pez(nombre,edad,"oceano",genero,"rojo", 6)
    
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return Pez(nombre,edad,"oceano",genero,"gris", 6)
    
    @classmethod
    def cantidadPeces(cls):
        return len(cls.listado)
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getCantidadAletas(self):
        return self.cantidadAletas