from funciones import alpha_x_y
from pyq import generaQ,generaP

def generarClave(nombre, carpeta):
	Q=generaQ()
	P,c=generaP(512,Q)
	Alpha,y,x=alpha_x_y(P,Q,c)
	
	f=open(carpeta+"/"+nombre+".cpub","w")
	f.write(str(P) + "\n")		
	f.write(str(Q)  + "\n")
	f.write(str(Alpha) + "\n")
	f.write(str(y))
	f.close()
	
	f=open(carpeta+"/"+nombre+".cpriv","w")
	f.write(str(x))		
	f.close()



if __name__ == "__main__":
	
	Q=generaQ()
	
	P,c=generaP(512,Q)
	
	Alpha,y,x=alpha_x_y(P,Q,c)
	
	
	f=open("fichero.cpub","w")
	f.write(str(P) + "\n")		
	f.write(str(Q)  + "\n")
	f.write(str(Alpha) + "\n")
	f.write(str(y))
	f.close()
	
	f=open("fichero.cpriv","w")
	f.write(str(x))		
	f.close()