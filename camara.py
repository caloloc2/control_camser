#!/usr/bin/python3
#Importamos librerias necesarias
import cv2 # para manejo de video y fotos
import MySQLdb # para manejo de base de datos

#funcion para guardar nombre de foto en base de datos
def guarda_bd(foto):
	db = MySQLdb.connect(host="localhost", user="root", passwd=" ", db="camara")
	cur = db.cursor()
	sql = "INSERT INTO fotos (foto) VALUES (%s)"
	val = (foto,)
	cur.execute(sql, val)
	db.commit()
	db.close()

camara = 0
vidcap = cv2.VideoCapture(camara)
success,image = vidcap.read()
count = 0
while success:
	success,image = vidcap.read()
	nombre_foto = "frame%d.jpg" % count
	cv2.imwrite(nombre_foto, image)
	guarda_bd(nombre_foto)
	count += 1
	if (count>20):
		break

"""
# Camara 0 es la camara web integrada, se debe cambiar la numeracion en caso de haber otros dispositivos
camara = 0
#Numero de fotogramas, mientras la camara se ajusta a los niveles de luz
fotogramas = 4
#iniciar camara
camera = cv2.VideoCapture(camara)
# Captura imagen  camara
def get_image():
	# leer la captura
	retval, im = camera.read()
	return im
for i in xrange(0, fotogramas):
	temp = get_image()
print("Foto tomada")
# entregar imagen leida anteriormente
camera_capture = get_image()
file = "fotos/captura.png"
# Guardar la imagen con opencv que fue leida por PIL
cv2.imwrite(file, camera_capture)
# finalizar camara
del(camera)