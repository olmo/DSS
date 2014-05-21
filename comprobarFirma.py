import hashlib
import sys
from funciones import potencia

def comprobarFirma(archivo, firma, cpub):
    f_archivo = open(archivo,'rb')
    f_firma = open(firma,'r')
    f_cpub = open(cpub,'r')
    
    p = int(f_cpub.readline())
    q = int(f_cpub.readline())
    alpha = int(f_cpub.readline())
    y = int(f_cpub.readline())
    
    r = int(f_firma.readline())
    s = int(f_firma.readline())
    
    u = int((int(hashlib.sha1(f_archivo.read()).hexdigest(),16)*(pow(s,q-2,q)))%q)
    v = int((r*(pow(s,q-2,q)))%q)
    
    r1 = ((potencia(alpha,u,p)*potencia(y,v,p))%p)%q
    
    f_archivo.close()
    f_firma.close()
    f_cpub.close()
    
    if r == r1:
        return True
    else:
        return False


if __name__ == "__main__":
    sol = comprobarFirma(sys.argv[1], sys.argv[2], sys.argv[3])

    if sol:
        print "Firma correcta"
    else:
        print "Firma incorrecta"
   