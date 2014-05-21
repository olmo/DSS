# Programa que dado cualquier fichero y un fichero de clave privada genera la firma DSS-DSA de ese primer fichero


import sys
import random
import hashlib
from funciones import potencia


def firmar (fichero_firmar, claves_publicas, clave_privada):
	# Lectura de los ficheros con las claves publicas y privada
	fi = open (claves_publicas)

	p = fi.readline()
	q = fi.readline()
	alpha = fi.readline()
	y = fi.readline()

	fi.close()

	fi = open (clave_privada)

	x = fi.readline()

	fi.close()


	# Apertura del fichero a firmar en binario
	fi = open (fichero_firmar, 'rb')


	# Convierto las cadenas a enteros
	p = int (p)
	q = int (q)
	alpha = int (alpha)
	y = int (y)
	x = int (x)


	k = int (random.uniform (2, q-1))  # Valor aleatorio (entre 2 y q-2, ambos incluidos) de un solo uso

	hash1_decimal = int(hashlib.sha1(fi.read()).hexdigest(), 16)  # Le aplico la funcion hash SHA-1 al fichero a firmar

	r = (potencia (alpha, k, p)) % q  # Valor r
	s = ((hash1_decimal + x * r) * potencia (k, q-2, q)) % q  # Valor s


	# Creo el fichero con la firma producida
	fo = open (fichero_firmar + ".firm", 'w')

	fo.write (str (r) + "\n")
	fo.write (str (s))

	fo.close()
	fi.close()



# Main
if __name__ == "__main__":
	fichero_firmar = sys.argv[1]
	claves_publicas = sys.argv[2]
	clave_privada = sys.argv[3]

	firmar (fichero_firmar, claves_publicas, clave_privada)
