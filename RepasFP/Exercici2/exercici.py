def interseccio(llista1, llista2):
    llista = [x for x in llista1 if x in llista2]
    return llista

def unio(llista1, llista2):
    llista = llista1 + [x for x in llista2 if x not in llista1]
    return llista

def multiplicacio_llistes(llista1, llista2):
    llista = [x*y for x,y in zip(llista1, llista2)]
    return llista

def multiplicacio_elements(llista1, llista2):
    llista = [[x*y for y in llista2] for x in llista1]
    return llista

def distancia_hamming(binari1, binari2):
    distancia = 0
    for i,j in zip(binari1, binari2):
        if i!=j:
            distancia+=1
    return distancia
