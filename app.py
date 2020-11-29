from flask import Flask

app = Flask (__name__)

@app.route('/')
def hellos():
    return "hello"

@app.route('/BuscarC', methods=['GET'])
def productos():
    return "mostrando productos"

@app.route('/CrearC', methods=['POST'])
def crear():
    return "Creando producto"

@app.route('/ActualizarC', methods=['PUT'])
def actualizar():
    return "Actualizando producto"

@app.route('/BorrarC', methods=['DELETE'])
def borrar():
    return "borrando producto"

if __name__  == "__main__":
    app.run(host='0.0.0.0')