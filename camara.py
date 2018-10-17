#!/usr/bin/python3
#Importamos librerias necesarias
import cv2 # para manejo de video y fotos
import MySQLdb # para manejo de base de datos
db = MySQLdb.connect(host="localhost", user="root", passwd=" ", db="camara")

#funcion para guardar nombre de foto en base de datos
def guarda_bd(foto):	
	cur = db.cursor()
	sql = "INSERT INTO fotos (foto) VALUES (%s)"
	val = (foto,)
	cur.execute(sql, val)
	db.commit()
	db.close()

def inicia():
	cur = db.cursor()
	sql = "TRUNCATE TABLE fotos"
	cur.execute(sql)
	db.commit()
	db.close()

camara = 0
vidcap = cv2.VideoCapture(camara)
success,image = vidcap.read()
count = 0

inicia()

while success:
	success,image = vidcap.read()
	nombre_foto = "frame%d.jpg" % count
	cv2.imwrite("fotos/"+nombre_foto, image)
	guarda_bd(nombre_foto)
	count += 1
	if (count>20):
		break