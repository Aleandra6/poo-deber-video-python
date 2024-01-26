class MiClase:
    def __init__(self):
        self.__atributo_privado = "Valor"
        
    def __habalr(self):
        print("hola como estas")    
        
objeto = MiClase()
print(objeto.__atributo_privado)
        
print(objeto.__habalr())        

        
        #lanza error porq __ significa q es muy privado
        