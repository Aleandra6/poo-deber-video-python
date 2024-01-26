class Notificador:
    def __init__(self, usuario, mensaje) :
        self.usuario = usuario
        self.mensaje = mensaje
        
    def notificar(self):
            raise NotImplementedError
        
       
class NotificadorEmail(Notificador):
    def Notificar(self):
        print(f"enviando mensaje a: {self.usuario.email}")
        
        
class NotificadorSMS(Notificador):
    def Notificar(self):
        print(f"enviando SMS a: {self.usuario.sms}")        
            
            
class NotificadorWathsap(Notificador):
    def Notificar(self):
        print(f"enviando Wathsap a: {self.usuario.wathsap}")        
        
        
        #programa extencible      