import numpy as np

def mostra_sudoku(sudoku):
    for fila in sudoku:
        for valor in fila:
            print (valor, ' ', end='')
        print(' ')

def inicialitza_n_lliures(sudoku):
    sudoku_l = list(sudoku.flat)
    return sudoku_l.count(0)

def es_valid(sudoku, numero, fila, columna):
    assert fila >= 0 and fila <= 9
    assert columna >= 0 and columna <= 9    
    assert numero >= 0 and numero <= 9    

    fila_inici_quadrat = int((fila - 1)/3)*3
    col_inici_quadrat = int((columna - 1)/3)*3
    valid = ( sudoku[fila - 1,columna - 1] == 0
		and numero not in sudoku[fila - 1,:]
    		and numero not in sudoku[:,columna - 1]
    		and numero not in sudoku[fila_inici_quadrat:fila_inici_quadrat+3,
				col_inici_quadrat:col_inici_quadrat+3])
    return valid

def juga_sudoku(nom_fitxer_sudoku):
    sudoku = np.loadtxt(nom_fitxer_sudoku, dtype='int')
    n_lliures = inicialitza_n_lliures(sudoku)
    mostra_sudoku(sudoku)
    numero = int(input("Numero: "))
    if numero != 0:
        fila = int(input("Fila: "))
        col = int(input("Columna: "))
    moviments_realitzats = []
    while (n_lliures != 0 and numero != 0):
        try:
            valid = es_valid(sudoku, numero, fila, col)
            if (valid):
                sudoku[fila - 1, col - 1] = numero
                n_lliures -= 1
            else:
                print ("Error. No es valid posar aquest numero en aquesta posicio")
        except:
           valid = False
           
        moviments_realitzats.append((numero, fila, col, valid))
        mostra_sudoku(sudoku)
            
        if n_lliures != 0:
            numero = int(input("Numero: "))
            if numero != 0:
                fila = int(input("Fila: "))
                col = int(input("Columna: "))
    if n_lliures == 0:
        print ("Enhorabona. Has completat el sudoku")
    return sudoku, moviments_realitzats


