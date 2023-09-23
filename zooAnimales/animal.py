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
        if self._zona:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}, la zona en la que me ubico es {self._zona}, en el {self._zona._zoo}"
        else:
            return f"Mi nombre es {self._nombre}, tengo una edad de {self._edad}, habito en {self._habitat} y mi genero es {self._genero}"

    @classmethod
    def totalAnimales(cls):
        return cls._totalAnimales
    
    @classmethod
    def totalPorTipo(cls):
        return "Mamiferos : " + str(cls.mamifero) +"\n" + "Aves : " + str(cls.ave) + "\n" + "Reptiles : " + str(cls.reptil) + "\n" + "Peces : " + str(cls.pez) + "\n" + "Anfibios : " + str(cls.anfibio)
    
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
        
    


