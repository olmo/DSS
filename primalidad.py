#!/usr/bin/python
import random
import funciones
import sys

def getA(P,lista):
    while True:
        aleatorio = random.randint(2,P-2)
        try:
            i = lista.index(aleatorio)
        except ValueError:
            break
    return aleatorio


def generaImpar(digitos):
    aleatorio = 2
    while aleatorio % 2 == 0:
        aleatorio= random.randint(10**(digitos-1),(10**digitos)-1)
    return aleatorio


	
def miller_Rabin(P,iteraciones):
    if P <= 5:
        return ("Entrada incorrecta N > 5 ")
    elif P%2 == 0:
		  return ("No es primo")

    es_prob_primo = False
    
    u = 0
    s = P-1
    
    while s % 2 == 0:
        u += 1
        s /= 2
    
    lista_usados=[]
    i = 0
    cont=0
    while cont < iteraciones:
        a = getA(P,lista_usados)
        lista_usados.append(a)
        a = funciones.potencia(a,s,P)
        if a != 1 and a != P-1:
            i = 1
            while i <= u-1:
                #print i
                a = funciones.potencia(a,2,P)
                if a == P-1:
                    es_prob_primo = True
                    i = u
                elif a == 1:
                   print a
                   return "No es primo"
                else:
                   pass
                i += 1
            if(es_prob_primo == False):
              return "no es primo"
        else:
            es_prob_primo = True
        cont +=1
        #probabilidad_act = ((4**i-1.0)/4**i)
    if es_prob_primo == True:
        return "Es probable primo"


if __name__ == "__main__":
    if len(sys.argv) == 3:
        print (miller_Rabin(int(sys.argv[1]),int(sys.argv[2])))
    else:
        print "Llamada incorrecta al programa <programa> <N> <iteraciones>"
