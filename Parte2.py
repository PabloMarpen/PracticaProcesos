import os, sys
fd = os.pipe()
leer = fd[0]
escribir = fd[1]



def procesarTexto(texto): #contar el número de líneas y palabras del archivo
    numLineas = 0
    numPalabras = 0
    
    lineas = texto.splitlines()
    
    for linea in lineas:
        numLineas += 1
        numPalabras += len(linea.split())

    salida = ("numlineas",numLineas, "numpalabras",numPalabras)
    return str(salida)

def padre():
    
    pid = os.fork() # te crea el proceso hijo y te da el PID del hijo
   
    
    if pid == 0:
        
        mensaje = os.read(leer, 1024).decode() #descodificamos el mensaje
        os.close(leer)
        mensajeparapadre = procesarTexto(mensaje) #lo pasamos a mayusculas
        os.write(escribir, mensajeparapadre.encode()) #codificamos el mensaje
        os.close(escribir) 
        
    else:
        
        # mensaje = "para hijo" # creamos el mensaje del padre al hijo
        
        f = open("fichero.txt", "r")
        textofichero = f.read() # leemos el mensaje para el hijo del txt
        
        # print("padre:",mensaje) # mostramos el original
        os.write(escribir, textofichero.encode()) #codificamos el mensaje
        os.wait()
        
        os.close(escribir)
        
        
        
        mensajerecibido = os.read(leer, 1024).decode() #descodificamos el mensaje
        os.close(leer)
        print("mensaje de hijo:", mensajerecibido)
        



padre()

