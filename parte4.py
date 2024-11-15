import subprocess  
import win32clipboard
def con():
    p1 = subprocess.Popen('ftp', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    comandos = [b"verbose\n",
                b"open ftp.freebsd.org\n",
                b"anonymous\n",
                b"password\n",
                b"get /pub/FreeBSD/README.TXT\n",] 

    for cmd in comandos:
        p1.stdin.write(cmd)

    respuesta = p1.communicate(timeout=15)[0]

    print(respuesta.decode("cp850", "ignore"))

def comparararchivo():
    f = open("readme.txt", "r")
    texto = f.read()

    win32clipboard.OpenClipboard()
    textoAnterior = win32clipboard.GetClipboardData()

    win32clipboard.EmptyClipboard()

    win32clipboard.SetClipboardText(texto)
    win32clipboard.CloseClipboard()
    win32clipboard.OpenClipboard()
    datosPosteriores = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    if textoAnterior != texto:
        print("el texto a cambiado de", textoAnterior, "a", texto)


opcion = "1"
while opcion == "1":
    con()
    comparararchivo()
    opcion = input("¿Quieres volver a conectarte? 1. sí 2. no: ")