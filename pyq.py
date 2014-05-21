import random
import primalidad

def generaAleatorio(numBits):
   numero = "1"
   cont = 0
   while cont < numBits-2:
      aleatorio = random.randint(0,1)
      cont+=1
      numero += str(aleatorio) 

   numero += "1"

   return numero

def binDecimal(numero):
   n=len(numero)
   valor=0
   for bit in numero:
      if bit == '1':
         valor=valor+2**(n-1)
      n -=1
   return valor

def generaP(numBits, q):
   if(numBits % 64 !=0):
      return "No es divisor de 64 el numero de bits"
   c = generaC(numBits)
   numero = c*q + 1
   resPrimo = primalidad.miller_Rabin(numero,40)
   while resPrimo == "no es primo":
      resPrimo = primalidad.miller_Rabin(numero,40)
      if(resPrimo == "no es primo"):
          #numero = numero + (2*q)
          c = c+2
          numero = c*q +1
   return numero,c
   

def generaC(numBits):
   bitsC = numBits - 160
   aleatorio = generaAleatorio(bitsC)
   aleatorioPar = binDecimal(aleatorio)
   aleatorioPar += 1
   return aleatorioPar
   
def generaQ():
   primo = generaAleatorio(160)
   probPrimo = binDecimal(primo)
   resPrimo = primalidad.miller_Rabin(probPrimo,40)

   while resPrimo == "no es primo":
      resPrimo = primalidad.miller_Rabin(probPrimo,40)
      if(resPrimo == "no es primo"):
          probPrimo +=2

   return probPrimo
if __name__ == "__main__":
   Q = generaQ()
   #print Q

   P,c = generaP(512,Q)
   #print P


