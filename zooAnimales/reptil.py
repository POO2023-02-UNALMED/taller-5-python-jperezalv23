from animal import Animal

class Reptil(Animal):
    listado = []
    serpientes = 0
    iguanas = 0
    def __init__(self, nombre, edad, habitat, genero, colorEscamas, largoCola):
        super().__init__(nombre, edad, habitat, genero)
        self.colorEscamas = colorEscamas
        self.largoCola = largoCola