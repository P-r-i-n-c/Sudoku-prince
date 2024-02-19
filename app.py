import json
from flask import Flask, request, jsonify
from Sudoku import convertir_tablero 
from Sudoku import ValidateSudoku  
app = Flask(__name__)

# Cargar el contenido del archivo ejemploTablero.json
with open('ejemploTablero.json', 'r') as file:
    ejemplo_tablero = json.load(file)

@app.route('/getsudoku', methods=['GET'])
def mostrar_sudoku():
    # Devolver el contenido del archivo como respuesta JSON
    return jsonify(ejemplo_tablero)

# @app.route('/sudoku', methods=['GET'])
# def mostrar_sudoku():
#     if request.method == 'GET':
#         # Obtener la lista enviada en el cuerpo del GET        
#         # Devolver el JSON como respuesta
#         return Sudoku.board
@app.route('/sudoku', methods=['GET'])
def lista_tablero():
    data = request.get_json()
    tablero_convertido = convertir_tablero(data)
    return tablero_convertido


@app.route('/sudokucheckfilascolumnas', methods=['POST'])
def sudokucheckfilascolumnas():
    data = request.get_json()
    tablero_convertido = convertir_tablero(data)
    tablero_convertido = json.loads(tablero_convertido)
    
    sudoku = ValidateSudoku(tablero_convertido)
    try:
        sudoku.chequeo_general()
        sudoku.chequeo_filas()
        sudoku.chequeo_columnas()
    except AssertionError as e:
        return jsonify({"mensaje": str(e), "tablero": tablero_convertido}), 400


    return jsonify({"mensaje": "El tablero de Sudoku ingresado es válido"}), 200

@app.route('/sudokucheckcuadrante', methods=['POST'])
def sudokucheckcuadrante():
    data = request.get_json()
    tablero_convertido = convertir_tablero(data)
    tablero_convertido = json.loads(tablero_convertido)
    
    sudoku = ValidateSudoku(tablero_convertido)
    try:
        sudoku.chequeo_general()
        sudoku.chequeo_subcuadros()
    except AssertionError as e:
        return jsonify({"mensaje": str(e), "tablero": tablero_convertido}), 400


    return jsonify({"mensaje": "Dato ubicado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)