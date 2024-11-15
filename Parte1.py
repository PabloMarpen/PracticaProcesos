import psutil


blocnotas = False
nombreProceso = input()

try:
        for proc in psutil.process_iter(['pid', 'name', 'cpu_times', 'memory_percent']):
                if proc.info['name'] == nombreProceso:
                        print(f''' 
                        Nombre {proc.info['name']}
                        PID    {proc.info['pid']}
                        CPU    {sum(proc.info['cpu_times'][:2][-3:])}
                        MEMORIA {proc.info['memory_percent']}
                        ''')
except Exception as e:
        print(f"error al leer el proceso: {e}")
        

def buscarProceso(nombreProceso):
        try:
                for proc in psutil.process_iter(['pid', 'name', 'cpu_times', 'memory_percent']):
                        if proc.info['name'] == nombreProceso:
                                return proc.info['pid']
        except Exception as e:
                print(f"error al leer el proceso: {e}")
        

print("escribe 'salir' para salir")
procesoName = input("dame el nombre del proceso: ")
while procesoName != "salir":
    try: 
            proceso = psutil.Process(int(buscarProceso(procesoName)))
            proceso.terminate()
            print("proceso cerrado con exito")
    except Exception as e:
            print(f"error al cerrar el proceso: {e}")

    print("escribe 'salir' para salir")
    procesoName = input("dame el nombre del proceso: ")


    