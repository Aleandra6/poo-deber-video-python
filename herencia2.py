class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalida = nacionalidad
        
    def hablar(self):
        print ("Hola estoy hablando")    
       
        
class Empleado(Persona):
   pass
        

            
                   
                   
Alejandro = Empleado("Roberto", 24, "Ecuatoriano")
Alejandro.hablar()


# para captura en vez de alejandro=empleado poner alejandro=persona
