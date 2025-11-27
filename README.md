# 💬 Chat Bidireccional con Sockets en Python

Este proyecto implementa un chat simple entre servidor y cliente usando sockets y Programación Orientada a Objetos. Ambos pueden enviar y recibir mensajes de forma simultánea mediante hilos.

---

## 🚀 Características
- Comunicación en tiempo real
- Arquitectura basada en POO
- Conexión mediante sockets TCP
- Implementación sencilla

---

## 📁 Archivos del proyecto

servidor.py
cliente.py


---

## ▶️ Cómo ejecutar

### 1. Ejecutar el servidor:
```bash
python servidor.py

python cliente.py
```

## Funcionamiento

El servidor crea un socket y queda en espera de una conexión.

El cliente se conecta al servidor mediante host y puerto.

Una vez conectados, tanto el cliente como el servidor utilizan dos hilos:

Un hilo para recibir mensajes.

Un hilo para enviar mensajes.

## Capturas de funcionamiento 

<img width="1183" height="184" alt="image" src="https://github.com/user-attachments/assets/94863b5d-764b-4fd7-a4a2-b572d3f64c36" />

<img width="914" height="149" alt="image" src="https://github.com/user-attachments/assets/fcc1904f-3f9c-49ff-baed-45786223696d" />

Este mecanismo permite comunicación bidireccional sin bloqueo y en tiempo real.



