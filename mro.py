class A:
    def hablar(self):
        print("hola desde A")
        
class B(A):
    pass

class C(A):
    def hablar(self):
        print("hola desde C")        
        
        
class D(B,C):
    pass       
        
d = D()

d.hablar()         

#para mostrar las capturas vamos borrando desde def y ponemos pass

        

                