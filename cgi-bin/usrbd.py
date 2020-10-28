#!/usr/bin/python3
import mysql.connector
import cgi

data = cgi.FieldStorage()

nombre = data.getvalue('nombre')
apellido = data.getvalue('apellido')
correo = data.getvalue('correo')
password = data.getvalue('password')

cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

cur.execute('select correo from usuarios')
tem = True

for i in cur:
    if correo in i:
        tem=False

print('Content-Type: text/html')
print('')
print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('<link rel="stylesheet" href="/CollarBone/css/registro_usr.css">')
print('<div class="card"> <h5 class="card-header"><i>Collarbone</i></h5> <div class="card-body">')

if (tem):
    sql = ("insert into usuarios values ('{}','{}','{}',SHA({}));".format(nombre,apellido,correo,password))
    cur.execute(sql)
    cnx.commit()
    print('<h7> Bienvenido <b>{}</b> ya eres parte de  <i>Collarbone.</i></h7>'.format(nombre))
    print('<div id = "contbtna"><a href="/CollarBone/index.html" id = "btna" class="badge badge-dark"> Ver camisetas!</a></div>')
else:
    print('<h7>El correo ingresado ya esta registrado.</h7>')
    print('<div id = "contbtna"><a href="/CollarBone/InicioSesion.html" class="badge badge-dark"> Inisiar Sesion</a></div>')
print('</div></div>')
cnx.close()










