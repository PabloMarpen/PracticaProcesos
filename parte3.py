from os import system 
import subprocess 
import asyncio  
import time

def showNotepad1():
    try:
        subprocess.run(['Notepad.exe', ])
    except subprocess.CalledProcessError as e:
        print(e.output)


async def showNotepad2():
    try:

        await asyncio.create_subprocess_exec('Notepad.exe')
    except subprocess.CalledProcessError as e:
       
        print(e.output)



async def main():

    opcion = input("elige la opcion 1. asincrono 2. sincrono")
    if (opcion == '1'):
        inicio = time.time()

        await showNotepad2()
        print("pulsa una tecla para terminar")
        system('Pause')

        fin = time.time()
        print(fin-inicio)
    elif (opcion == '2'):
        inicio = time.time()
        showNotepad1()
        fin = time.time()
        print(fin-inicio)
    else:
        print("opcion no contemplada")

asyncio.run(main())