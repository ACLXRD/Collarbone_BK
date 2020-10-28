#!/usr/bin/python3
import hashlib
import base64
import mysql.connector
import cgi


data = cgi.FieldStorage()

NombreCamiseta = data.getvalue('NombreCamiseta')
NumeroCamisetasDisponibles = data.getvalue('NumeroCamisetasDisponibles')
TallasDisponibles = data.getvalue('TallasDisponibles')
PrecioCamiseta = data.getvalue('PrecioCamiseta')
ImagenCamiseta = data.getvalue('ImagenCamiseta')

cnx = mysql.connector.connect (user='root', password = '1234', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()

cur.execute('select NombreCamiseta from camisetas')
tem = True

for i in cur:
    if NombreCamiseta in i:
        tem=False

print('Content-Type: text/html')
print('')
print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('<link rel="stylesheet" href="/CollarBone/css/registro_usr.css">')
print('<div class="card"> <h5 class="card-header"><i>Collarbone</i></h5> <div class="card-body">')

if (tem):
    sql = ("insert into camisetas values ('{}',{},'{}',{},'{}')".format(NombreCamiseta,NumeroCamisetasDisponibles,TallasDisponibles,PrecioCamiseta,ImagenCamiseta))
    cur.execute(sql)
    cnx.commit()
    print('<h7> Creación Exitosa. La camiseta <b>{}</b> ya se encuentra en inventario<i>Collarbone.</i></h7>'.format(NombreCamiseta))
    print('<div id = "contbtna"><a href="/CollarBone/administracion.html" id = "btna" class="badge badge-dark">Regresar</a></div>')
else:
    print('<h7>La camiseta ingresada ya existe</h7>')
    print('<a href="/CollarBone/administracion.html" class="badge badge-dark">Regresar</a>')
cnx.close()
print('</div></div>')




