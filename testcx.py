#!/usr/bin/python3
#Codigo para probar la conexión con la base de datos
import mysql.connector
from mysql.connector import errorcode
try:
  cnx = mysql.connector.connect(user='aclr', password = '1010029624',
  database='usuarios', host='127.0.0.1')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
     print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
     print("Database does not exist")
  else:
     print(err)
else:
   cnx.close()





