class Persona:
    def __init__ (self,nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
            
    def set_nombre(self, new_nombre):
         self._nombre = new_nombre        
            
Alejandra = Persona("Ana",22)

nombre = Alejandra.get_nombre()
print(nombre)

Alejandra.set_nombre("Sara")

nombre = Alejandra.get_nombre()
print(nombre)