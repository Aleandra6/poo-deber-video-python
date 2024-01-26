class Persona:
    def __init__ (self,nombre, edad):
        self.__nombre = nombre
        self._edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
        
    @nombre.setter        
    def nombre(self, new_nombre):
        self.__nombre = new_nombre
                
    @nombre.deleter      
    def nombre(self, new_nombre):
        del self.__nombre 
                            
         
            
Alejandra = Persona("Ana",22)

nombre = Alejandra.nombre
print(nombre)


Alejandra.nombre = "Sara"

nombre = Alejandra.nombre
print(nombre)


#del Alejandra.nombre  