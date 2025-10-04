import time
import RPi.GPIO as GPIO

# --- Configuración del Pin ---
PIN_SENSOR_IR = 17 # Cambia este pin si tu sensor está conectado a otro

# --- Inicialización ---
def setup():
    # Establece el modo de numeración de pines a BCM
    GPIO.setmode(GPIO.BCM)
    
    # Configura el pin del sensor como entrada (Input) con pull-up interno
    GPIO.setup(PIN_SENSOR_IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    print("Sistema iniciado. Presiona Ctrl+C para salir.")

# --- Bucle Principal ---
def loop():
    while True:
        # Lee el estado del pin del sensor
        # Lógica común: LOW (0) = Objeto detectado; HIGH (1) = Camino libre
        estado_sensor = GPIO.input(PIN_SENSOR_IR)
        
        if estado_sensor == GPIO.LOW:
            print(f"OBSTÁCULO DETECTADO. (Señal: {estado_sensor})")
        else:
            print(f"Camino despejado. (Señal: {estado_sensor})")
        time.sleep(0.5)

# --- Limpieza al salir ---
def destroy():
    GPIO.cleanup()
    print("\nPrograma finalizado y pines GPIO liberados.")

# --- Ejecución del Programa ---
if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        destroy()