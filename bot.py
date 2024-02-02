import github
import os
import requests
import base64

# Authenticate with GitHub using a personal access token
g = github.Github("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")

# Get the repository
repo = g.get_user().get_repo("repobotnet")

# Define la URL del archivo .passwd en GitHub
url = 'https://raw.githubusercontent.com/yasjavi/repobotnet/main/.passwd'

def download_passwd():
    print('[!] Descargando .passwd')
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content.decode('utf-8')
        with open(".passwd", 'w') as file:
            file.write(content)
        print('[!] .passwd descargado con éxito.')
    else:
        print('[-] Fallo al descargar .passwd. Código de estado:', response.status_code)

# Descarga .passwd y lo almacena localmente
download_passwd()

# Abre el archivo .passwd en modo binario
with open(".passwd", "rb") as f:
    # Crea un nuevo archivo en el repositorio
    repo.create_file(".passwd", "Actualizando .passwd en el repositorio", f.read())
