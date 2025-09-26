#librerias a usar 
import time
import RPi.GPIO as GPIO

# Configuración del pin del led
LED_PIN = 4

# inicializacion
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(1)
except KeyboardInterrupt:
    print("FIN")
finally:
    GPIO.cleanup()


