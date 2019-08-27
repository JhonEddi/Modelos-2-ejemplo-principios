import math

class Figura():
    
    def obtenerArea(self)
        
    
class Cuadrado(Figura):
    
    def __init__(self,l):
        self.__L = l
        
    def obtenerArea(self):
        return self.__L*self.__L
        
class Rectangulo(Figura):
    
    def __init__(self,b,h):
        self.__b = b
        self.__h = h
        
    def obtenerArea(self):
        return self.__b*self.__h
        
class Circulo(Figura):
    
    def __init__(self,r):
        self.__r = r
        
    def obtenerArea(self):
        return math.pow(self.__r,2)*math.pi
        
def iniciar():
    print("Seleccione una opcion ","\n","1) cuadrado","\n","2) rectangulo")
    n = int(input("Selecione: "))
    
    if (n==1):
        l = int(input("Ingrese el lado del cuadrado: "))
        figura = Cuadrado(l)
    if (n==2):
        b = int(input("Ingrese la base del rectangulo: "))
        h = int(input("Ingrese la altura del rectangulo: "))
        figura = Rectangulo(b,h)
    if (n==3):
        r = int(input("Ingrese el radio del circulo: "))
        figura = Circulo(r)   
        
    print("El area de la figura es: ",figura.obtenerArea())
    
iniciar()