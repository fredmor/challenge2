# challenge2
Agente y servidor para monitoreo remoto

1.1 Requerimientos transversales:
-	Python 3.7 > 
Nota: si la instalación de Python no incluye el gestor de paquetes “pip” este se debe instalar mediante el siguiente comando: sudo apt update && apt install python3-pip
1.2 Requerimiento en servidor que será monitoreado:
Instalar librería de Python psuti: 
-	Linux: $ sudo pip3 install psutil
-	Windows: pip install psutil
1.3 Requerimiento en servidor de API:
Instalar framework de Python Flask: 
-	Linux: $ sudo pip3 install flask
-	Windows: pip3 install flask
2. EJECUCION DE APLCIACIONES:
La solución cuenta con 2 archivos:
-	agente.py: Script que recolecta la información y envía al servidor central para su almacenamiento en archivos .json
-	api.py: Script que se ejecuta en el servidor central y recibe la información del agente para almacenarla.

IMPORTANTE: La aplicación agente.py tiene configurada una IP local 127.0.0.1 como la IP del servidor central al cual le enviará la información, por lo tanto, para la prueba se ejecutó el agente agente.py y la aplicación api.py en un mismo servidor para confirmar el buen funcionamiento. Si la prueba de la solución se realizará en diferentes servidores se requiere que se cambie la IP en la línea # 47 del archivo agente.py, como se observa a continuación

![image](https://user-images.githubusercontent.com/18684247/118325718-7b994300-b4c9-11eb-8981-cd502590f83d.png)

2.1 Ejecución de servidor (api.py):
Linux: sudo python3 api.py
Windows: Python api.py
2.2 Ejecución agente (agente.py)
Linux: sudo python3 agente.py
Windows: Python agente.py
2.3 Resultado:
Después de la ejecución del agente y el api se debería observar un archivo nuevo con formato json como se observa a continuación:

![image](https://user-images.githubusercontent.com/18684247/118325788-966bb780-b4c9-11eb-9df1-b3d66fbe9220.png)
