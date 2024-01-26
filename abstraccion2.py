#clase abstracta
from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre, edad,sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f'hola me llamo: {self.nombre} y tengo {self.edad}años')
        
        
class Estudiante(Persona):            
    def __init__(self,nombre, edad,sexo, actividad):
        super().__init__(nombre, edad,sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy estudiando: {self.actividad}") 
        
class Trabajador(Persona):            
    def __init__(self,nombre, edad,sexo, actividad):
        super().__init__(nombre, edad,sexo, actividad)
        
    def hacer_actividad(self):
        print(f"Estoy trabajando en el area de: {self.actividad}")            
        
Alejandra = Estudiante("Ana",23, "Femenino", "Contabilidad")      
Sara = Trabajador("Ana",23, "Femenino", "Contabilidad") 

Alejandra.hacer_actividad()  
Alejandra.presentarse()

Sara.hacer_actividad()
Sara.presentarse()