from animal import Animal

class Reptil(Animal):
    listado = []
    serpientes = 0
    iguanas = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola
        Animal.reptil += 1
        Reptil.listado.append(self)

    @classmethod
    def crearIguana(cls, nombre, edad, genero):
        cls.iguanas += 1
        return Reptil(nombre,edad,"humedal",genero,"verde", 3)
    
    @classmethod
    def crearSerpiente(cls, nombre, edad, genero):
        cls.serpientes += 1
        return Reptil(nombre,edad,"jungla",genero,"blanco", 1)
    
    @classmethod
    def cantidadReptiles(cls):
        return len(cls.listado)
    
    def getColorEscamas(self):
        return self.colorEscamas
    
    def getLargoCola(self):
        return self.largoCola