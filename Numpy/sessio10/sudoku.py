import numpy as np
import time

def es_valid_list(sudoku, numero, fila, columna):  
    fila_inici_quadrat = int(fila/3)*3
    col_inici_quadrat = int(columna/3)*3
    col = [f[columna] for f in sudoku]
    quadrat = [f[col_inici_quadrat:col_inici_quadrat+3] for f in sudoku[fila_inici_quadrat:fila_inici_quadrat+3]]
    valid = ( sudoku[fila][columna] == 0
		and numero not in sudoku[fila]
        and numero not in col
        and all([numero not in fila for fila in quadrat]))
    return valid

def es_valid(sudoku, numero, fila, columna):  
    fila_inici_quadrat = int(fila/3)*3
    col_inici_quadrat = int(columna/3)*3
    valid = ( sudoku[fila,columna] == 0
		and numero not in sudoku[fila,:]
    		and numero not in sudoku[:,columna]
    		and numero not in sudoku[fila_inici_quadrat:fila_inici_quadrat+3,
				col_inici_quadrat:col_inici_quadrat+3])
    return valid

def test_sudoku(nom_fitxer_sudoku):
    sudoku = np.loadtxt(nom_fitxer_sudoku, dtype='int')
    numero = int(input("Numero: "))
    fila = int(input("Fila: "))
    col = int(input("Columna: "))
    
    start = time.time()
    for i in range(100000):
        valid = es_valid(sudoku, numero, fila, col)
    end = time.time()
    print (end - start)
    if (valid):
        print("El numero SI es valid a aquesta posicio")
    else:
        print("El numero NO es valid a aquesta posicio")
    sudoku_list = sudoku.tolist()
    start = time.time()
    for i in range(100000):
        valid = es_valid_list(sudoku_list, numero, fila, col)
    end = time.time()
    print (end - start)
    if (valid):
        print("El numero SI es valid a aquesta posicio")
    else:
        print("El numero NO es valid a aquesta posicio")


if __name__ == "__main__":
    test_sudoku("sudoku1.txt")