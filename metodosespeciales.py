class perosna:
    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad
        
        
    def __str__ (self):
        return f'perosna(nombre={self.nombre}, edad={self.edad})'
    
    def __repr__(self):
        return f'perosna(nombre="{self.nombre}", edad={self.edad})'
    
    def __add__(self,otro):
        nuevo_valor = self.edad + otro.edad
        return perosna (self.nombre + otro.nombre, nuevo_valor)
        
alejandra = perosna("Ana",23)        
sara = perosna("sant",4)

nueva_perosna = alejandra+sara
print(nueva_perosna.nombre)
# print(alejandra)


# # lista =(1,2,3)
# # print(lista)

# repre= repr(alejandra)

# resultado = eval(repre)

# print(resultado.nombre)


