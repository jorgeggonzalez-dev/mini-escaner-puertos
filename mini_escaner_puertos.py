import socket
import ipaddress
# 1. Define el objetivo (Tu dispoditivo) y el puerto que queremos revisar:
print("\n--- MINI-ESCANER DE PUERTOS INTERACTIVO ---")

while True:
  while True:
   try:
      ip_entrada = input("\nIntroduce la IP a escanear (o escribe 'salir'): ").strip()   
      if ip_entrada.lower() == 'salir':
         print("¡Gracias por usar el escáner!")
         exit()
      ip_objetivo = str(ipaddress.ip_address(ip_entrada))
      break
   except ValueError:
      print("Añade un IP valido")

  while True:
   try:
     puerto = int(input("Puerto: "))
     break
   except ValueError:
     print("Añade un puerto valido")
 
# 2. Creamos el conector (el "teléfono" para llamar a la IP)
  conexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 3. Límite de tiempo de 2 segundos para que no se quede esperando siempre
  conexion.settimeout(2.0)

# 4. Intentamos conectar. El método 'connect_ex' devuelve un 0 si la conexión fue exitosa
  print(f"Escaneando {ip_objetivo} en el puerto {puerto}...")
  resultado = conexion.connect_ex((ip_objetivo, puerto))

# 5. Mostrar el resultado en pantalla
  if resultado == 0:
    print(f"¡El puerto {puerto} está ABIERTO!")
  else:
    print(f"El puerto {puerto} está cerrado o bloqueado.")

# 6. Cerrar el conector por seguridad
  conexion.close()
