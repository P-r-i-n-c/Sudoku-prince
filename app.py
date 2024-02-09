from flask import Flask, request, jsonify
import Sudoku
import json


app = Flask(__name__)

@app.route('/sudoku', methods=['GET'])
def mostrar_sudoku():
    if request.method == 'GET':
        # Obtener la lista enviada en el cuerpo del GET        
        # Devolver el JSON como respuesta
        return Sudoku.board


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

#         # Devolver el tablero Sudoku actualizado
#     return jsonify({"mensaje":"No se puede añadir, intenta con otro numero"}), 

# @app.route('/sudoku', methods=['PUT'])
# def añadir_numero_sudoku():
#     # Obtener los datos del JSON enviado en la solicitud
#     json_data = request.get_json()
#     #pasa el json a una lista 
    
#     # Verificar si la posición es válida utilizando la función isValid()
#     if all(SudokuFuncs.isValid() for in json_data):        # La posición es válida, así que actualiza el tablero y devuelve el JSON actualizado
        
#         return json_data
    
#     # Si la posición no es válida, devuelve un mensaje de error
#     return jsonify({"mensaje": "No se puede añadir, intenta con otro número"}), 400

    
if __name__ == '__main__':
    app.run(debug=True)