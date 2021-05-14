#IMPORTAMOS LIBRERIAS.
import psutil
import platform
import json
import requests


#FUNCION PARA REPRESENTAR TAMAÑOS EN BITS.
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#INFORMACIÓN DE LA CPU
print("="*20, "CPU", "="*20)
#Nº NUCLEOS
cpuv = {'cpu':platform.uname().processor}
cpujson = json.dumps(cpuv)

#PROCESOS
print("="*20, "PROCESOS", "="*20)
procesos = ""
for proc in psutil.process_iter(['pid', 'name', 'username']):
    procesos = procesos+" "+str(proc.info)

procnj = {'procesos':procesos}
procjson = json.dumps(procnj)

#USUARIOS
print("="*20, "USUARIOS", "="*20)
usernj = {'usuarios':psutil.users()}
userjson = json.dumps(usernj)

#INFORMACIÓN BÁSICA DEL SISTEMA.
print("="*20, "SISTEMA OPERATIVO", "="*20)
uname = platform.uname()

sysnj = {'sistema':'SO:'+uname.system+'---Nombre: '+uname.node+'---Version: '+uname.release}
sysjson = json.dumps(sysnj)

# ENVIO DE DATOS A SERVER
info = {"Informacion":[{"cpu":platform.uname().processor}, {"procesos":procesos},{"usuarios":psutil.users()},{"sistema":sysnj}]}
datos = json.dumps(info)

respuesta = requests.post("http://127.0.0.1:8080/data", json = datos)