class Animal:
    _totalAnimales = 0
    anfibio = 0
    ave = 0
    pez = 0
    mamifero = 0
    reptil = 0
    def __init__(self, nombre, edad, habitat, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitat = habitat
        self._genero = genero
        self._zona = None
        Animal._totalAnimales += 1

    def toString(self):
        if self.zona:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}, la zona en la que me ubico es {self.zona}, en el {self.zona.zoo}"
        else:
            return f"Mi nombre es {self.nombre}, tengo una edad de {self.edad}, habito en {self.habitat} y mi genero es {self.genero}"

    @classmethod
    def totalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos: " + cls.mamifero +"\n" + "Aves: " + cls.ave + "\n" + "Reptiles: " + cls.reptil + "\n" + "Peces: " + cls.pez + "\n" + "Anfibios: " + cls.anfibio
    
    def getNombre(self):
        return self._nombre
    
    def getGenero(self):
        return self._genero
    
    def getEdad(self):
        return self._edad
    
    def getHabitat(self):
        return self._habitat
    
    def setNombre(self,Nnombre): 
        self._nombre=Nnombre

    def setGenero(self,genero): 
        self._genero= genero
        
    def setEdad(self,edad): 
        self._edad= edad
    
    def setHabitat(self,habitat): 
        self._habitat= habitat
        
    


