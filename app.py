import json
from flask import Flask, request, jsonify


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



@app.route('/sudoku', methods=['POST'])
def recibir_tablero():
    data = request.get_json()  # Obtener los datos del cuerpo de la solicitud POST
    posicionx = data["posicionx"]
    posiciony = data["posiciony"]
    numero = data["numero"]
    tablero = data["tablero"]

    # Calcular la posición total
    posicion =  posicionx * posiciony
    
    # Verificar que la posición esté en el rango correcto (0-80)
    if 1 <= posicion <= 27:
        # Contador para llevar la cuenta de las celdas exploradas
        celdas_exploradas = 0
        # Iterar sobre las filas del tablero
        for fila in tablero:
            # Iterar sobre las columnas de la fila
            for columna in fila["columnas"]:
                # Iterar sobre las celdas de la columna
                for col in columna:
                    # Si la celda es cero y hemos llegado a la posición indicada
                    if celdas_exploradas == posicion:
                        # Asignar el número a la celda
                        columna = numero
                        # Crear un nuevo diccionario solo con el tablero actualizado
                        tablero_actualizado = {"tablero": tablero}
                        return jsonify(tablero_actualizado)
                    # Incrementar el contador de celdas exploradas
                    celdas_exploradas += 1
    else:
        return "Error: La posición está fuera de rango (0-80)", 400
    
    # En caso de que no se haya encontrado una celda válida para colocar el número
    return "Error: No se pudo colocar el número en la posición indicada", 400


if __name__ == '__main__':
    app.run(debug=True)