#!/usr/bin/python3
#Dependencias utilizadas
import mysql.connector
import cgi

data = cgi.FieldStorage()

# Se obtienen los daots del frontend para su respectva insersión en la BD
NombreCamiseta = data.getvalue('NombreCamiseta')
NumeroCamisetasDisponibles = data.getvalue('NumeroCamisetasDisponibles')
TallasDisponibles = data.getvalue('TallasDisponibles')
PrecioCamiseta = data.getvalue('PrecioCamiseta')
ImagenCamiseta = data.getvalue('ImagenCamiseta')

# Se establece conexión con la BD
cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()

#Sentencia SQL para la verificación: Si la camiseta existe no se puede proceder con la creación
cur.execute('select Nombre from camisetas')
tem = True

for i in cur:
    if NombreCamiseta in i:
        tem=False

#Metadatos HTML para hoja de estilos y enlace a Bootstrap
print('Content-Type: text/html')
print('')
print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('<link rel="stylesheet" href="/CollarBone/css/registro_usr.css">')
print('<div class="card"> <h5 class="card-header"><i>Collarbone</i></h5> <div class="card-body">')

if (tem):
    #Sentencia SQL para la insersión (creación) de una nueva camiseta.
    sql = ("insert into camisetas values ('{}',{},'{}',{},'{}')".format(NombreCamiseta,NumeroCamisetasDisponibles,TallasDisponibles,PrecioCamiseta,ImagenCamiseta))
    cur.execute(sql)
    cnx.commit()
    print('<h7> Creacion Exitosa. La camiseta <b>{}</b> ya se encuentra en el inventario y página de <i> Collarbone.</i></h7>'.format(NombreCamiseta))
    print('<div id = "contbtna"><a href="/CollarBone/administracion.html" id = "btna" class="badge badge-dark">Regresar</a></div>')
else:
    #Aviso en pantalla si la camiseta ya existe
    print('<h7>La camiseta "{}" ya existe</h7>'.format(NombreCamiseta))
    print('<div id = "contbtna"><a href="/CollarBone/administracion.html" class="badge badge-dark">Modificar ?</a></div>')
cnx.close()
print('</div></div>')




