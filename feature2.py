import datetime
import socket

# Obtener la hora actual
hora_actual = datetime.datetime.now().strftime("%H:%M:%S")

# Obtener la dirección IP de la máquina
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f"Hora actual: {hora_actual}")
print(f"Dirección IP: {ip_address}")
