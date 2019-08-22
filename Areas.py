class Cuadradrilatero:
		def operacion (b,h):
			print "Ingrese valor de la base y luego la altura:";
			if l!= None and h!=None:
				return l*h;
			return "No es posible";

class Triangulo:
		def operacion (b,h):
			print "Ingrese valor de la base y luego la altura:";
			if b!= None and h!=None:
				return (b*h)/2;
			return "No es posible";

def figura (figura,b,h):
		if figura==1:
			return Cuadradrilatero(b,h);
		if figura==2:
			return Triangulo(b,h);
		return "No es posible realizar la accion";