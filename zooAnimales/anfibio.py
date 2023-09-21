from animal import Animal

class Anfibio(Animal):
    listado = []
    ranas = 0
    salamandras = 0
    def __init__(self, nombre, edad, habitat, genero, colorPiel, venenoso):
        super().__init__(nombre, edad, habitat, genero)
        self.colorPiel = colorPiel
        self.venenoso = venenoso