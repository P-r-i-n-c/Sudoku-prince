import json
from flask import Flask, request, jsonify
import Sudoku


app = Flask(__name__)

# Cargar el contenido del archivo ejemploTablero.json
with open('ejemploTablero.json', 'r') as file:
    ejemplo_tablero = json.load(file)

@app.route('/sudoku', methods=['GET'])
def mostrar_sudoku():
    # Devolver el contenido del archivo como respuesta JSON
    return jsonify(ejemplo_tablero)

# @app.route('/sudoku', methods=['GET'])
# def mostrar_sudoku():
#     if request.method == 'GET':
#         # Obtener la lista enviada en el cuerpo del GET        
#         # Devolver el JSON como respuesta
#         return Sudoku.board


@app.route('/sudoku', methods=['POST'])
def validar_sudoku():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud POST

    # Validar el tablero de Sudoku
    sudoku_validator = Sudoku.ValidateSudoku(data)
    sudoku_validator.chequeo_general()
    sudoku_validator.chequeo_filas()
    sudoku_validator.chequeo_columnas()
    sudoku_validator.chequeo_subcuadros()

    # Si no se generó ninguna excepción, el tablero es válido
    return jsonify({'mensaje': 'El tablero de Sudoku ingresado es válido'})

if __name__ == '__main__':
    app.run(debug=True)