from zooAnimales.animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso
        Animal.anfibio += 1
        Anfibio.listado.append(self)

    @classmethod
    def crearRana(cls, nombre, edad, genero):
        cls.ranas += 1
        return Anfibio(nombre,edad,"selva",genero,"rojo", True)
    
    @classmethod
    def crearSalamandra(cls, nombre, edad, genero):
        cls.salamandras += 1
        return Anfibio(nombre,edad,"selva",genero,"negro y amarillo", False)
    
    @classmethod
    def cantidadAnfibios(cls):
        return len(cls.listado)
    
    def isVenenoso(self):
        return self.venenoso
    
    def getColorPiel(self):
        return self.colorPiel
    
    
    
