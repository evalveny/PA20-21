import numpy as np

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
    valid = es_valid(sudoku, numero, fila, col)
    if (valid):
        print("El numero SI es valid a aquesta posicio")
    else:
        print("El numero NO es valid a aquesta posicio")


if __name__ == "__main__":
    test_sudoku("sudoku1.txt")