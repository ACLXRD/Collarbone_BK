#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_cors import CORS
import mysql.connector

# Se establece conexión con la BD
cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

DEBUG = True
app = Flask (__name__)
app.config.from_object(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})

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

@app.route('/CrearC', methods=['POST'])
def crear():
    return "Creando producto"

@app.route('/ActualizarC', methods=['PUT'])
def actualizar():
    return "Actualizando producto"

@app.route('/BorrarC', methods=['DELETE'])
def borrar():
    print("-----> entra")
    data = request.get_json(force=True)
    print("-----> {}".format(data))
    sup = data.get('supC')
    print("-----> {}".format(sup))
    sql = "delete from camisetas WHERE (Nombre = '{}');".format(sup)
    cur.execute(sql)
    print("-----> Query exed")
    return "Camiseta eliminada"

if __name__  == "__main__":
    app.run(host='0.0.0.0')