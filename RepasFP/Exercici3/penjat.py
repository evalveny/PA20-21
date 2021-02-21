def comprova_paraula(paraula, paraula_actual, lletra):
    correcte = False
    nova_paraula_actual = ''
    for i,c in enumerate(paraula):
        if (c == lletra):
            correcte = True
            nova_paraula_actual = nova_paraula_actual + c
        else:
            nova_paraula_actual = nova_paraula_actual + paraula_actual[i]           
    if '-' not in nova_paraula_actual:
        endevinat = True
    else:
        endevinat = False
    return endevinat, correcte, nova_paraula_actual

def juga_penjat(paraula, max_errors):
    paraula_actual = '-' * len(paraula)
    print("Estat del joc: ", paraula_actual)
    n_errors = 0
    endevinat = False
    lletres_entrades=[]    
    resultat = []
    while not endevinat and n_errors < max_errors:
        lletra = input("Introdueix una lletra: ")
        if lletra in lletres_entrades:
            print("Error. Aquesta lletra ja l'havies introduït")
            resultat.append("ERROR")
        else:
            endevinat, correcte, paraula_actual = comprova_paraula(paraula, paraula_actual, lletra)
            if not correcte:
                n_errors += 1
                print("Aquesta lletra no està a la paraula, Errors: ", n_errors)
            print("Estat del joc: ", paraula_actual)
            resultat.append(paraula_actual)
        lletres_entrades.append(lletra)

    if correcte:
        print("HAS GUANYAT!!!")
    else:
        print("HAS PERDUT!!! La paraula era " + paraula)
    return endevinat, lletres_entrades, resultat




