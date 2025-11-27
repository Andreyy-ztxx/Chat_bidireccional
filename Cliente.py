import socket
import threading

class ClienteChat:
    def __init__(self, host="localhost", puerto=5000):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host
        self.puerto = puerto

    def conectar(self):
        self.socket.connect((self.host, self.puerto))
        print("Conectado al servidor")

    def recibir_mensajes(self):
        while True:
            try:
                mensaje = self.socket.recv(1024).decode()
                print("Servidor:", mensaje)
            except:
                print("Servidor desconectado")
                break

    def enviar_mensajes(self):
        while True:
            mensaje = input("")
            self.socket.send(mensaje.encode())

    def iniciar(self):
        self.conectar()

        hilo_recibir = threading.Thread(target=self.recibir_mensajes)
        hilo_recibir.start()

        hilo_enviar = threading.Thread(target=self.enviar_mensajes)
        hilo_enviar.start()


if __name__ == "__main__":
    cliente = ClienteChat()
    cliente.iniciar()
