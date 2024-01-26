class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalida = nacionalidad
        
    def hablar(self):
        print ("Hola estoy hablando")    
       
        
class Empleado(Persona):
   def __init__ (self,nombre, edad, nacionalidad, trabajo, salario):
       super().__init__(nombre, edad, nacionalidad)
       self.trabajo = trabajo
       self.salario = salario
        
   def hablar(self):
        print ("Hola")    
               
                   
                   
Alejandro = Empleado("Roberto", 24, "Ecuatoriano", "Militar", 200000)

Alejandro.hablar()