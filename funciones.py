import random

def potencia (a, b, p):

	if not b >= 1 or not p >= 2:
		return 'ERROR!! Parametros incorrectos (uso: b >= 1 y p >= 2)'

	x = 1

	while b != 1:
		if b % 2 == 1:
			x = (x * a) % p

		a = (a ** 2) % p
		b = b // 2

	x = (x * a) % p

	return x  # Devuelvo a^b (mod p)

def alpha_x_y(P,Q,c):
	
	#Calculo de Alpha:
	#Basado en http://es.wikipedia.org/wiki/DSA
	h=		random.randint(2,P-2)
	alpha=	potencia(h,c,P)	
	x=		random.randint(2,Q-2)
	y=		potencia(alpha,x,P)
	
	
	return alpha, y, x
