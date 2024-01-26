class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalida = nacionalidad
        
       
        
class Empleado(Persona):
   pass
        

            
                   
                   
Alejandro = Empleado("ANGEL", 24, "Ecuatoriano")
print (Alejandro.nacionalida)
print(Alejandro.edad)
print(Alejandro.nombre)
                   