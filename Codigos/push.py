#librerias a usar 
import time
import RPi.GPIO as GPIO

# Configuración de pines
LED_PIN = 4
BUTTON_PIN = 17  # Cambia este pin si tu botón está conectado a otro

# Inicialización
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-up interno

try:
    while True:
        if GPIO.input(BUTTON_PIN) == GPIO.LOW:  # Botón presionado
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
