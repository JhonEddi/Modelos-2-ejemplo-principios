import areas
print ("Calcular Áreas \n")
print ("1.Cuadrilatero \n2.Triangulo")

x=int(input("Escoja Figura: "))

if x==1:
  L=int(input('Ingrese el lado: '))
  Areas.area_Cuadrilatero(L)

if x==2:
  b=int(input('Ingrese la base: '))
  h=int(input('Ingrese la altura: '))
  Areas.area_triangulo(b,h)
  
if x>2:
  return print ("No existe esta opción")
