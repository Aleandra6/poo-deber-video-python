class Celulares:
    def __init__(self, marca,modelo,camara):
    
       self.marca = marca
       self.modelo = modelo
       self.camara = camara
    def llamar(self):
        print(f'Estas llamando desde: {self.modelo} ')
    def cortar(self):
        print(f"Estas cortando desde: {self.modelo}")
                  
    
celular1 = Celulares("Samsung", "S23", "48MP")

     
    
print (celular1.camara)
    

celular1.cortar()

