from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector
import cgi

# Se establece conexión con la BD
cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

DEBUG = True
app = Flask (__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

data = cgi.FieldStorage()
nombreC = "Worlds Parallels"
print(nombreC)
nombreC = data.getvalue('nombreCx')
print(nombreC)

@app.route('/')
def hellos():
    return "hello"

@app.route('/BuscarC', methods=['GET'])
def productos(): 
    sql = "select * from camisetas;"
    cur.execute(sql)
    camisetas = cur.fetchall()
    print(camisetas)
    listac = list()
    if camisetas:
        for i in camisetas:
            nombre = i[0]
            cantidad = i[1]
            tallas = i[2]
            precio = i[3]
            url = i[4]
            camiseta = {"nombre": nombre, 'cantidad': cantidad, 'tallas': tallas, 'precio':precio, 'url':url}
            listac.append(camiseta)
        return jsonify(data=listac)
    return "Fallo en consulta"

@app.route('/BuscarCone', methods=['GET'])
def producto(): 
    print(nombreC)
    sql = "select * from camisetas where Nombre = '{}';".format(nombreC)
    cur.execute(sql)
    camisetas = cur.fetchall()
    print(camisetas)
    listac = list()
    if camisetas:
        for i in camisetas:
            nombre = i[0]
            cantidad = i[1]
            tallas = i[2]
            precio = i[3]
            url = i[4]
            camiseta = {"nombre": nombre, 'cantidad': cantidad, 'tallas': tallas, 'precio':precio, 'url':url}
            listac.append(camiseta)
        return jsonify(data=listac)
    return "Fallo en consulta"

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