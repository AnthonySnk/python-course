import sqlite3

miConexion=sqlite3.connect("pythonDB") #!Abriendo la base de datos

miCursor=miConexion.cursor()
# miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")#!Escrbir instruccion SQL

# miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALÓN',15,'DEPORTES')")

# variospProductos=[
#     ("CAMISETA",10,"DEPORTES"),
#     ("JARRÓN",90,"CERAMICA"),
#     ("CAMIÓN",20,"JUGUETERIA")
# ]
# miCursor.executemany("INSERT INTO PRODUCTOS VALUES(?,?,?)",variospProductos)#!LOS SIGNOS DE ? SON  SEGUN LOS CAMPOS QUE TENEMOS

miCursor.execute("SELECT * FROM PRODUCTOS")
#PARA ALMACENAR EL QUERY
infoSelect=miCursor.fetchall()
# print(infoSelect)
for producto in infoSelect:
    print(producto[0])

miConexion.commit()#!Confirmando los cambios

miConexion.close() #!Terminando la conexion
