import socket
import threading

class ServidorChat:
    def __init__(self, puerto=5000):
        self.puerto = puerto
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("0.0.0.0", self.puerto))
        self.server_socket.listen(1)
        print(f"Servidor iniciado en puerto {self.puerto}")
        self.cliente = None

    def aceptar_conexion(self):
        print("Esperando conexión del cliente...")
        self.cliente, direccion = self.server_socket.accept()
        print(f"Cliente conectado desde {direccion}")

    def recibir_mensajes(self):
        while True:
            try:
                mensaje = self.cliente.recv(1024).decode()
                print("Cliente:", mensaje)
            except:
                print("Cliente desconectado")
                break

    def enviar_mensajes(self):
        while True:
            mensaje = input("")
            self.cliente.send(mensaje.encode())

    def iniciar(self):
        self.aceptar_conexion()

        hilo_recibir = threading.Thread(target=self.recibir_mensajes)
        hilo_recibir.start()

        hilo_enviar = threading.Thread(target=self.enviar_mensajes)
        hilo_enviar.start()


if __name__ == "__main__":
    servidor = ServidorChat()
    servidor.iniciar()
