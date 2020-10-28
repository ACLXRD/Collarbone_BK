#!/usr/bin/python3
import mysql.connector
import cgi

data = cgi.FieldStorage()

correo = data.getvalue('correo')
password = data.getvalue('password')

cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

sql = ("select * from usuarios where correo = '{}' and password_ = SHA('{}'); ".format(correo,password))
cur.execute(sql)
usrcheck = cur.fetchall()
nombre = ":p"
admin = False

if usrcheck:
    sql = ("select nombre from usuarios where correo = '{}'".format(correo))
    cur.execute(sql)
    find = cur.fetchall()
    for row in find:
        nombre = row[0]
    usrcheck = True
    sql2 = ("select * from administrador where correo = '{}'".format(correo))
    cur.execute(sql2)
    admin = cur.fetchall()

print('Content-Type: text/html')
print('')

print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('<link rel="stylesheet" href="/CollarBone/css/registro_usr.css">')
print('<div class="card"> <h5 class="card-header"><i>Collarbone</i></h5> <div class="card-body">')

if(admin):
    print('<h7> Bienvenido de nuevo <b>Admin. {}</b> a <i>Collarbone.</i></h7>'.format(nombre))
    print('<div id = "contbtna"><a href="/CollarBone/administracion.html" id = "btna"  class="badge badge-dark">Vamos!</a></div>')
    print('<script> location.href="/CollarBone/administracion.html";</script>')
elif (usrcheck):
    print('<h7> Bienvenido de nuevo <b>{}</b> a <i>Collarbone.</i></h7>'.format(nombre))
    print('<a href="/CollarBone/intodex.html" id = "btna"  class="badge badge-dark"> Ver camisetas!</a>')
    print('<script> location.href="/CollarBone/intodex.html";</script>')
else:
    print('<h7>El correo o el password  ingresados no existen.</h7>')
    print('<div id = "contbtna">Deseas <a href="/CollarBone/registro_usr.html" class="badge badge-dark"> ¿Registrarse?</a></div>')
cnx.close()
print('</div></div>')