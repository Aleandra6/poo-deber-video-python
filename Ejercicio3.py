class Animal:
    def comer(self):
        print("El animal esta comiendo")
        
class Ave(Animal):
    def volar(self):
        print("El ave esta volando")
                
class Mamifero(Animal):
    def amamantar(self):
        print("El mamifero esta amamantando")
  
class Murcielago(Mamifero,Ave):
    pass



mamifero = Mamifero()

mamifero.comer()
mamifero.amamantar()

murcielago = Murcielago()

murcielago.comer()
murcielago.volar()
murcielago.amamantar()

ave =Ave()

ave.comer()
ave.volar()

animal = Animal()

animal.comer()

print(Murcielago.mro())


                                