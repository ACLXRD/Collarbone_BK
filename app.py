from flask import Flask
import mysql.connector

# Se establece conexión con la BD
cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()


app = Flask (__name__)

@app.route('/')
def hellos():
    return "hello"

@app.route('/BuscarC', methods=['GET'])
def productos():
    sql = "select * from camisetas;"
    cur.execute(sql)
    camisetas = cur.fetchall()
    return camisetas

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