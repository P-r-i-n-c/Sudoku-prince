import json

board = []

def convertir_tablero(response):
    # Extraer el tablero actualizado
    tablero_actualizado = response["tablero"]
    # Inicializar la lista para el tablero

    # Recorrer cada tablero en la lista de tableros
    for fila in tablero_actualizado:
        # Recorrer cada fila del tablero
        for celdas in fila["columnas"]:
            # Convertir la lista de números en la fila a una lista de strings
            valores_celda = [str(numero) for lista in celdas for numero in lista]
            # Extender la lista del tablero con los valores de las celdas
            board.extend(valores_celda)

    # Dividir la lista en sublistas de 9 elementos cada una
    board_divided = [board[i:i+9] for i in range(0, len(board), 9)]

    # Formatear la lista board para guardarla en una variable
    board_formatted = ['\n[' + ','.join(['"' + celda + '"' for celda in fila]) + ']' for fila in board_divided]
    board_output = '[' + ','.join(board_formatted) + ']'

    return board_output

class ValidateSudoku:
    def __init__(self, tablero) -> None:
        self.tablero = tablero
        self.lista_invertida = list()

    def chequeo_general(self):
        """
        Chequear que el tablero introducido sea un tablero 9x9 
        """
        #assert 
        assert len(self.tablero) == 9, "El tablero ingresado no respeta el formato 9x9" #filas
        for fila in self.tablero:
            assert len(fila) == 9, "El tablero ingresado no respeta el formato 9x9"

    
    def chequeo_filas(self, lista_a_chequear='tablero_general'):
        if lista_a_chequear == 'tablero_general':
            lista_a_chequear = self.tablero

        for fila in lista_a_chequear:
            for elemento in fila:
                if elemento != '0':
                    assert fila.count(elemento) == 1, "El tablero no es valido"


    def chequeo_columnas(self):

        for column_index in range(0,9):
            for row_index in range(0,9):
                self.lista_invertida.append(self.tablero[row_index][column_index])
            
            self.chequeo_filas([self.lista_invertida])

            self.lista_invertida.clear()


    def chequeo_subcuadros(self):
        #funcion mayor
        #tenemos 9 subcuadros = chequear de 3 en 3
        # de mis primeras 3 filas -> subcuadros del 0 al 3, 3 al 6, 6 al 9
        self.chequeo_3_subcuadros(0,3)
        self.chequeo_3_subcuadros(3,6)
        self.chequeo_3_subcuadros(6,9)

    def chequeo_3_subcuadros(self, rango1, rango2):
        self.lista_invertida.clear()
        for row_index in range(0,9):
            if row_index == 3 or row_index == 6:
                self.lista_invertida.clear()
            for column_index in range(rango1,rango2):
                self.lista_invertida.append(self.tablero[column_index][row_index])
                if len(self.lista_invertida) == 9:
                    self.chequeo_filas([self.lista_invertida])
                #chequeo filas