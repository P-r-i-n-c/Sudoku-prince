from flask import Flask, request, jsonify
import SudokuFuncs
import json


app = Flask(__name__)

@app.route('/sudoku', methods=['GET'])
def mostrar_sudoku():
    if request.method == 'GET':
        # Obtener la lista enviada en el cuerpo del GET
        json_MyBoard = SudokuFuncs.json_MyBoard
        
        # Devolver el JSON como respuesta
        return json_MyBoard

@app.route('/sudoku', methods=['PUT'])
def añadir_numero_sudoku():
    new_json_sudoku = request.json
    listaSudoku = json.dumps(new_json_sudoku)
    if (SudokuFuncs.isValid(board, row, col, num) for board in new_json_sudoku
        for row in new_json_sudoku for col in new_json_sudoku for num in new_json_sudoku):
        return listaSudoku 
    
        
        # Devolver el tablero Sudoku actualizado
    return jsonify({"mensaje":"No se puede añadir, intenta con otro numero"}), 
    
    
if __name__ == '__main__':
    app.run(debug=True)