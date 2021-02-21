import math

def suma_acumulada(llista):
    resultat = [sum(llista[:i+1]) for i in range(len(llista))]
    return resultat


def factorial(n):
    fact = 1
    for x in range(1,n+1):
        fact = fact*x
    return fact

def factorial_llista(llista):
    resultat = [factorial(x) for x in llista]
    return resultat

def es_primer(n):
    if (n <= 3):
        return True
    else:
        divisor = 2
        while ((divisor < math.sqrt(n)) and ((n % divisor) != 0)):
            divisor = divisor + 1
        return ((n % divisor) != 0)
    
def primers(llista):
    resultat = [x for x in llista if es_primer(x)]
    return resultat

def elimina_duplicats(llista):
    resultat = [x for i,x in enumerate(llista) if x not in llista[:i]]
    return resultat

def binari_decimal(binari):
    decimal = 0
    potencia = 1
    for x in binari[1:]:
        potencia = potencia * 2
        decimal = 2*decimal + x
    if (binari[0] == 1):
        decimal = decimal - potencia
    return decimal