#DIP

# class Diccionario:
#      def verifcar_palabra(self,palabra):
#          #Logica para verifcar palabras
#          pass

# class CorrectorOrtográfico:
#        def __init__(self):
#          self.dicionario = Diccionario()

#        def corregir_texto(self, texto):
#             #usamos el diccionario para corregir el texto
#             pass

from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
         pass
     #logica para verificar palabra
     
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        pass
    #logica para verificar palabra si esta en el diccionario
    
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self,palabra):
        pass
    #logica para verificar palabra desde el servicio online
        
class CorrectorOrtografico:
    def __init__ (self, verificador) :
        self.verificador = verificador
        
    def corregir_texto(self, texto):
        self.texto = texto    
        #usamso verificador para corregir texto
        
corrector =CorrectorOrtografico(ServicioOnline())        