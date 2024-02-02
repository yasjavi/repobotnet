import github
import requests
import base64

# Autenticación con GitHub usando un token de acceso personal
g = github.Github("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")

# Obtener el repositorio
repo = g.get_user().get_repo("repobotnet")

# Definir la URL del archivo a descargar
url = 'https://raw.githubusercontent.com/yasjavi/repobotnet/main/.passwd'

def download_file():
    print('[!] Descargando .passwd')
    response = requests.get(url)
    if response.status_code == 200:
        content = response.content
        with open(".passwd", 'wb') as file:
            file.write(content)
        print('[!] .passwd descargado con éxito.')
    else:
        print('[-] Fallo al descargar .passwd. Código de estado:', response.status_code)

def upload_file():
    print('[!] Subiendo .passwd al repositorio')
    with open(".passwd", "rb") as file:
        # Crear un nuevo archivo en el repositorio
        repo.create_file(".passwd", "Actualizando .passwd en el repositorio", file.read())
    print('[!] .passwd cargado con éxito en el repositorio.')

# Descargar el archivo
download_file()

# Subir el archivo al repositorio
upload_file()

