#!/usr/bin/python3
import mysql.connector
import cgi 

cnx = mysql.connector.connect (user='aclr', password = '1010029624', database='Collarbone', host='127.0.0.1')
cur = cnx.cursor()
cnx.commit()

# sql = ("select COUNT(URLImagen) from camisetas;")
# # cur.execute(sql)
# nrows = cur.execute(sql);

sql = ("select URLImagen from camisetas")
cur.execute(sql)
camisetas = cur.fetchall()
  
print('Content-Type: text/html; charset=utf-8\n\r' )
print('')
print('<!DOCTYPE html>')
print('<html lang="en">')
print('<head>')
print('    <meta charset="UTF-8">')
print('    <meta name="viewport" content="width=device-width, initial-scale=1.0">')
print('    <meta http-equiv="X-UA-Compatible" content="ie=edge">')
print('    <link rel="shortcut icon" type="image/x-icon" href="/CollarBone/img/skull.ico">')
print('    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous">')
print('    <link rel="stylesheet" href="/CollarBone/css/menu.css" />')
print('    <link rel="stylesheet" href="/CollarBone/css/estilos.css" />')
print('    <link rel="stylesheet" href="/CollarBone/css/footer.css" />')
print('    <title>Collarbone</title>')
print('    <link href="https://fonts.googleapis.com/css?family=Istok+Web:400,700|Playball&display=swap" rel="stylesheet">')
print('</head>')
print('<body id="index">')
print('    <div id="box1">')
print('        <div id="box2">')
print('            <h1><a href="/CollarBone/index.html" id="name">Collarbone</a></h1>')
print('        </div>')
print('        <div id="box3">')
print('            <ul id="menu">')
print('                <li><a href="/CollarBone/index.html">Inicio</a></li>')
print('                <li><a href="#">Categorias</a></li>')
print('                <li><a href="/CollarBone/InicioSesion.html">Ingresar</a></li>')
print('                <li><a href="/CollarBone/registro_usr.html">Registrarse</a></li>')
print('                <li><a href="https://api.whatsapp.com/send?phone=573195806765&text=Hola,%20tengo%20una%20pregunta%20" target="_blanck">Chat</a></li>')
print('            </ul>')
print('        </div>')
print('    </div>')
print('    <div id="inicio">')
print('        <img src="/CollarBone/img/pic1.jpg" alt="Collarbone" width="100%">')
print('        <div class="tl1">Collarbone</div>')
print('        <div class="tl1" id="arrow1">↡</div>')
print('    </div>')
print('    <h2 id="pregal">Destacadas</h2>')
print('    <div id="update">')
print('        <form action="/cgi-bin/Collarbone_BK/ondex.py">')
print('        <input type="submit" value="Actualizar" class="btn btn-primary" id="btnupd">')
print('        </form>')
print('    </div>')
print('    <div id="box4" margin="auto">')
print('        <table class="galeria">')

cont = 0
for row in reversed(camisetas):
    cont+=1
    if(cont == 1):
        print('<tr>')
    print('<td> <a class="linkc" href="#"><img src="{}" alt="Camiseta X" width="422" height="562"></a></td>'.format(row[0]))
    if (cont == 3):   
        print('</tr>')
        cont=0

print('        </table>')
print('    </div>')
print('    <footer>')
print('        <div class="container-footer-all">')
print('             <div class="container-body">')
print('                 <div class="colum1">')
print('                     <h1>Redes Sociales</h1>')
print('                     <div class="row">')
print('                        <a target="_blanck" href="https://www.instagram.com/collarbone_shirts/"></ahref><img src="/CollarBone/img/LogoIG.png" ></a>')
print('                        <label>Siguenos en Instagram</label>')
print('                    </div>')
print('                     <div class="row">')
print('                        <a target="_blanck" href="https://www.facebook.com/Collarbone-104201821177244/?modal=admin_todo_tour"><img src="/CollarBone/img/LogoFB.png"></a>')
print('                         <label>Siguenos en Facebook</label>')
print('                     </div>')
print('                     <div class="row">')
print('                        <a target="_blanck" href="https://twitter.com/Collarb40200108"><img src="/CollarBone/img/LogoTW.png"></a>')
print('                         <label>Siguenos en Twitter</label>')
print('                     </div>')
print('                     <div class="row">')
print('                        <a target="_blanck" href="https://co.pinterest.com/collarboneshirts/"><img src="/CollarBone/img/LogoPT.png"></a>')
print('                         <label>Siguenos en Pinterest</label>')
print('                     </div> ')
print('                 </div>')
print('                 <div class="colum2">')
print('                     <h1>Contactanos</h1>')
print('                     <div class="row">')
print('                         <img src="/CollarBone/img/LogoUB.png">')
print('                         <label>Cl. 74 #14-14 Universidad Sergio Arboleda</label>')
print('                     </div>')
print('                     <div class="row">')
print('                         <img src="/CollarBone/img/LogoWA.png">')
print('                         <label>(57) 3195806765 </label>')
print('                     </div>')
print('                     <div class="row">')
print('                         <img src="/CollarBone/img/LogoGM.png">')
print('                          <label>Collarbone@gmail.com</label>')
print('                     </div>')
print('                 </div>')
print('             </div>')
print('        </div>')
print('        <div class="container-footer">')
print('            <div class="footer">')
print('                <div class="copyright">')
print('                    © 2020 Todos los Derechos Reservados | <a target="_blanck" href="">Collarbone</a>')
print('                </div>')
print('                <div class="information">')
print('                    <a target="_blanck" href="">Informacion Compañia</a> | <a target="_blanck" href="">Privacion y Politica</a> | <a target="_blanck" href="">Terminos y Condiciones</a>')
print('                </div>')
print('            </div>')
print('        </div>')
print('    </footer>')
print('</body>')
print('')
print('</html>')