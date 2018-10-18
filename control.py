import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT) ## GPIO 26 como salida
GPIO.setup(19, GPIO.OUT) ## GPIO 19 como salida
GPIO.setup(13, GPIO.OUT) ## GPIO 13 como salida
GPIO.setup(6, GPIO.OUT) ## GPIO 6 como salida

def movimientos():
	archivo = open("movimientos.txt", "r")
	lin = archivo.read()
	archivo.close()
    return lin

while True:
    valor = movimientos()
    if (valor=="1"):
        GPIO.output(26, True)
        time.sleep(.100)
        GPIO.output(26, False)
    elif (valor=="2"):
        GPIO.output(19, True)
        time.sleep(.100)
        GPIO.output(19, False)
    elif (valor=="3"):
        GPIO.output(13, True)
        time.sleep(.100)
        GPIO.output(13, False)
    elif (valor=="4"):
        GPIO.output(6, True)
        time.sleep(.100)
        GPIO.output(6, False)
    else:
        # apaga todos los leds
        GPIO.output(26, False)
        GPIO.output(19, False)
        GPIO.output(13, False)
        GPIO.output(6, False)

GPIO.cleanup()