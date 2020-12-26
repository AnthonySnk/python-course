#-*-coding:utf-8 -*-
import sqlite3

miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

#!SELECT
miCursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confección'")
infoSelec = miCursor.fetchall()
print(infoSelec)
#!UPDATE
miCursor.execute("UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")
#!DELETE


miConexion.commit()
miConexion.close()