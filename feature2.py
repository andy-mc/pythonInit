import datetime
import socket

# Obtener la hora actual
hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

# Obtener la dirección IP de la máquina
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hora actual: {hora_actual}")
print(f"Dirección IP: {ip_address}")

# Calcular el tiempo de ejecución
tiempo_inicio = datetime.datetime.now()

# Simular algún procesamiento
import time
time.sleep(1)  # Espera 1 segundo para demostración

tiempo_fin = datetime.datetime.now()
tiempo_ejecucion = tiempo_fin - tiempo_inicio

print(f"Tiempo de ejecución: {tiempo_ejecucion.total_seconds():.2f} segundos")


