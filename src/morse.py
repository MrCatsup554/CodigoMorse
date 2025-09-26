#librerias a usar 
import time
import RPi.GPIO as GPIO

# Configuración del pin del led
LED_PIN = 

# inicializacion
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

def punto():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.5)  # 1 Hertz (0.5 segundos)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)  

def raya():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(0.333)  # 3 Hertz (0.333 segundos)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(0.5)  

def S():
    punto()
    punto()
    punto()

def O():
    raya()
    raya()
    raya()

def sos():
    S()
    O()
    S()

try:
    sos()
finally:
    GPIO.cleanup()