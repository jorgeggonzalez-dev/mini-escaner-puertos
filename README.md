# Mini Escáner de Puertos Interactivo 🔒🌐

Un script interactivo y sencillo desarrollado en **Python** para auditar y verificar el estado de puertos específicos en un dispositivo de red. Ideal para entender los fundamentos de las conexiones de red y el uso de sockets en ciberseguridad.

## 🚀 Características
* **Validación de IP:** Utiliza el módulo `ipaddress` para garantizar que el objetivo ingresado tenga un formato IPv4 o IPv6 válido.
* **Control de Errores:** Manejo de excepciones en la entrada del usuario (tanto para direcciones IP como para números de puerto).
* **Escaneo Seguro:** Implementa un `timeout` de 2 segundos para evitar que el script se quede colgado esperando respuestas en puertos bloqueados.
* **Bucle Interactivo:** Permite realizar múltiples consultas consecutivas sin necesidad de reiniciar el script, con una opción de salida limpia (`salir`).

## 🛠️ Tecnologías y Módulos Utilizados
* **Python 3**
* **Socket:** Para el manejo de las conexiones de red a bajo nivel (TCP).
* **Ipaddress:** Para la validación técnica y estructurada de las direcciones IP.

## 📋 Requisitos Previos
No requiere instalar dependencias externas, ya que utiliza bibliotecas nativas de Python. Solo asegúrate de tener Python instalado.
