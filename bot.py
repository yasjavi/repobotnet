import subprocess
 
def run():
    subprocess.run(["echo", "Hello world"], check=True, text=True)
