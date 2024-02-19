from azure.communication.email import EmailClient
import json
from flask import Flask, request, jsonify
from Sudoku import convertir_tablero 
from Sudoku import ValidateSudoku  
app = Flask(__name__)

def correo_mal():
    try:
        connection_string = "endpoint=https://prog3.unitedstates.communication.azure.com/;accesskey=26pmLQHFeg/sfCb7WlxkvbzngnOSeB9QzplyVXpJnG1hwCH+f8iLJ7QxE5au9vDGJcYmUM5fAt0o62tuGy4itQ=="
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@bd846568-501c-422a-ae4e-142a2e8da0b5.azurecomm.net",
            "recipients":  {
                "to": [{"address": "cachacoposting@gmail.com" }],
            },
            "content": {
                "subject": "No se pudo ubicar",
                "plainText": "“message”:”El dato no puede ser ubicado, cambie de posición”.",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)
def correo_bien():
    try:
        connection_string = "endpoint=https://prog3.unitedstates.communication.azure.com/;accesskey=26pmLQHFeg/sfCb7WlxkvbzngnOSeB9QzplyVXpJnG1hwCH+f8iLJ7QxE5au9vDGJcYmUM5fAt0o62tuGy4itQ=="
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@bd846568-501c-422a-ae4e-142a2e8da0b5.azurecomm.net",
            "recipients":  {
                "to": [{"address": "cachacoposting@gmail.com" }],
            },
            "content": {
                "subject": "Correo electrónico de prueba",
                "plainText": "“message”:”Dato ubicado correctamente”",
            }
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)



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
        correo_mal()
        return jsonify({"mensaje": str(e), "tablero": tablero_convertido}), 400

    correo_bien()
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
        correo_mal()
        return jsonify({"mensaje": str(e), "tablero": tablero_convertido}), 400

    correo_bien()
    return jsonify({"mensaje": "Dato ubicado correctamente"}), 200

if __name__ == '__main__':
    app.run(debug=True)