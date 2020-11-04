#!/usr/bin/python3
#Dependencias utilizadas
import mysql.connector
import cgi 

#Se extablece conexión con la base de datos
cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

#Sentencia SQL para la consulta de una camiseta.
sql = ("select * from camisetas where imagen = 'https://www.mattelsa.net/media/catalog/product/cache/1/small_image/657x/17f82f742ffe127f42dca9de82fb58b1/5/1/51797-1.jpg';")
cur.execute(sql)
find = cur.fetchall()
nombre = ""
imagen = ""
des = ""
#Se ectra cada dato de la consulta SQL
for row in find:
    nombre = row[0]
    des = row[1]
    imagen = row[2] 

#Codigo HTML 
print('Content-Type: text/html')
print('')
print('<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('<link rel="stylesheet" href="/CollarBone/css/camiseta.css">')
print('<link rel="shortcut icon" type="image/x-icon" href="/CollarBone/img/icono.ico"> <link rel="stylesheet" href="/CollarBone/css/menu.css" /> <link rel="stylesheet" href="/CollarBone/css/camiseta.css" />    <link rel="stylesheet" href="/CollarBone/css/footer.css" />    <title>Collarbone</title><link href="https://fonts.googleapis.com/css?family=Istok+Web:400,700|Playball&display=swap" rel="stylesheet"><link href="https://fonts.googleapis.com/css?family=Roboto:400,500&display=swap" rel="stylesheet"></head>')
print('<div id="box1"><div id="box2"><h1><a href="/CollarBone/index.html" id="name">Collarbone</a></h1></div><div id="box3"><ul id="menu"><li><a href="/CollarBone/index.html">Inicio</a></li><li><a href="">Categorias</a></li><li><a href="/CollarBone/InicioSesion.html">Ingresar</a></li><li><a href="/CollarBone/registro_usr.html">Registrarse</a></li> <li><a href="https://api.whatsapp.com/send?phone=573195806765&text=Hola,%20tengo%20una%20pregunta%20" target="_blank">Chat</a></li></ul></div></div>')
print('<div id="contenedor">')
print('<div id="boximg"><img src="{}" alt="Camiseta X" class="img-fluid img-thumbnail" width="422" height="562"></div>'.format(imagen))
print('<div id="boxdescrip">')
print('<h2>{}</h2><br/><br/>'.format(nombre))
print('<p>{}</p>'.format(des))
print('<p id="btnpedir">')
print('<a target="_blank" href="https://api.whatsapp.com/send?phone=573195806765&text=Hola,%20me%20envias%20la%20camiseta%20">Pedir</a>')
print('</p>')
print('</div>')
print('</div>')
print('<br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br /><br />')
print('<footer>')
print('<div class="container-footer-all">')
print('<div class="container-body">')
print('<div class="colum1">')
print('<h1>Redes Sociales</h1>')
print('<div class="row">')
print('<a target="_blanck" href="https://www.instagram.com/collarbone_shirts/"></ahref><img src="/CollarBone/img/LogoIG.png"></a>')
print('<label>Siguenos en Instagram</label>')
print('</div>')
print('<div class="row">')
print('<a target="_blanck" href="https://www.facebook.com/Collarbone-104201821177244/?modal=admin_todo_tour"><img src="/CollarBone/img/LogoFB.png"></a>')
print('<label>Siguenos en Facebook</label>')
print('</div>')
print('<div class="row">')
print('<a target="_blanck" href="https://twitter.com/Collarb40200108"><img src="/CollarBone/img/LogoTW.png"></a>')
print('<label>Siguenos en Twitter</label>')
print('</div>')
print('<div class="row">')
print('<a target="_blanck" href="https://co.pinterest.com/collarboneshirts/"><img src="/CollarBone/img/LogoPT.png"></a>')
print('<label>Siguenos en Pinterest</label>')
print('</div>')
print('</div>')
print('<div class="colum2">')
print('<h1>Contactanos</h1>')
print('<div class="row">')
print('<img src="/CollarBone/img/LogoUB.png">')
print('<label>Cl. 74 N 14-14 Universidad Sergio Arboleda</label>')
print('</div>')
print('<div class="row">')
print('<img src="/CollarBone/img/LogoWA.png">')
print('<label>57 3195806765 </label>')
print('</div>')
print('<div class="row">')
print(' <img src="/CollarBone/img/LogoGM.png">')
print('<label>Collarbone@gmail.com</label>')
print('</div>')
print('</div>')
print('</div>')
print('</div>')
print('<div class="container-footer">')
print('<div class="footer">')
print('<div class="copyright">')
print('© 2020 Todos los Derechos Reservados | <a target="_blanck" href="">Collarbone</a>')
print('</div>')
print('<div class="information">')
print('<a target="_blanck" href="">Informacion Compañia</a> | <a target="_blanck" href="">Privacion y Politica</a> | <a target="_blanck" href="">Terminos y Condiciones</a>')
print('</div>')
print('</div>')
print('</div>')
print('</footer>')

