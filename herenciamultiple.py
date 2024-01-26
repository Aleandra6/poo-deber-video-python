class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalida = nacionalidad
        
    def hablar(self):
        print ("Hola estoy hablando")    
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad 
        
    def mostrar_habilidad(self):
        return(f"Mi habilidad es: {self.habilidad}")    
        
class EmpleadoArtista(Persona, Artista):
    def __init__ (self, nombre, edad, nacionalidad, habilidad, empresa, salario):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario  = salario
        self.empresa = empresa 
        
    
           
        
    def presentarse(self):
         print (f'Hola soy: {self.nombre}, {self.mostrar_habilidad()} y trabajo de {self.empresa}')
           
         
        
Alejandro = EmpleadoArtista("Alejandro", 24, "Ecuatoriano","Cantar", "Militar", 200000)                        

Alejandro.presentarse()


herencia = issubclass(EmpleadoArtista,Artista)
instancia = isinstance(Alejandro,EmpleadoArtista)
print (instancia)
print(herencia)