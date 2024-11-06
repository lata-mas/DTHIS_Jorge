# DTHIS

 El dispositivo DTHIS mide las variables de interes dentro del area de diseño bioclimático. En el contexto de la construción de un nuevo edificio para la LIER en el IER, se emplearon estrategias bioclimáticas dentro del mismo y la única manera de comprobar que dichas estrategias funcionan, es a través de los datos que el DTHIS pueda darnos. EL DTHIS (Dispositivo de Temperatura, Humedad, Iluminación y Sonido) funciona con un microprocesador Raspberry Pi y 3 sensores/hardware diferentes, los cuales a través de una seria de códigos recolectan las variables de interes y las mandan a una plataforma de internet de las cosas como  Thingsboard.


## Piezas del DTHIS

| **Sensor**                                    | **Variable**                       | **Cantidad** |   **Link**                                                                                        |
|-----------------------------------------------|------------------------------------|--------------|---------------------------------------------------------------------------------------------------|
| SCD30 Sensirion                               | Temperatura, CO₂ y Humedad Relativa| 1            | (https://www.agelectronica.com/detalle.php?p=101020634*)                                          |
| Fisheye Camera                                | Luminancia                         | 1            | (https://www.agelectronica.com/detalle.php?p=SKU10344*)                                           |
| Micrófono ambiental USB                       | dB Maximos, minimos y promedio     | 1            | (https://www.steren.com.mx/microfono-usb-c-de-solapa-para-celular.html)                           | 
| Ventilador y disipador                        |                                    | 1            | (https://www.330ohms.com/products/ventilador-con-disipador-de-calor?_pos=3&_sid=9bcb8693a&_ss=r)  |
| Raspberry Pi 4 Model B                        | Microprocesador                    | 1            | (https://www.330ohms.com/collections/raspberry-pi-4/products/raspberry-pi-4-modelo-b-2gb)         |
| POE                                           |                                    | 1            | (https://www.agelectronica.com/detalle.php?p=RASPBERRYPI-POE%sumHAT)                              | 

## Elementos del repositorio
 
- #### En [**CAD**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/CAD) encuentra
	- Planos para 3D de la carcasa


 - #### En [**manual**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/manual) encuentra
	- Manual de operación para recrear el DTHIS

 - #### En [**codigo**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/codigo) encuentra
	- Códigos empleados en el SCD30, medición de niveles de ruido, mapas de luminancia, 
 - 
 - #### En [**diagramas**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/diagramas) encuentra
	- Imagenes de los diagramas de conexión usados en la documentación

## Preparar la Raspberry 


  1. Instalar sistema operativo en la microSD [buscar un video YT y ligarlo]
  2. Crear un ambiente virtual  de Python llamado dthis en un folder venvs en el home [video]

Para preparar el ambiente virtual, debes instalar los paquetes de requirements.txt

1. Activa el entorno virtual:
```bash
source venvs/dthis/bin/activate
```
2. Instala las dependencias desde el archivo `requirements.txt`:
```bash
python -m pip install -r requirements.txt
```

- ## SCD30
 - ### 1. Habilitar comunicación
1. Se teclea lo siguiente en la terminal para entrar al menu de configuración
```bash
sudo raspi-config
```
2. Nos dirigimos al apartado `Interface Options`.
3. Habilitar **I2C**
4. Reinicias la _Raspi_

 - ### 2. Conexión del SCD30
Sigue el siguiente diagrama:
![SCD30](diagramas/SCD30.png)

- ### 3. Script de Python
Ejecuta el script [scd30.py](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/SCD30.py). 

- ## Micrófono
  
### 1. Armado de circuito

En este caso usaremos un microfono USB-C al cual le pusimos un adaptador de C-USB. Antes de conectar el micrófono debes apagar la _Raspi_

### 2. Descargar paqueterias necesarias 
```
sudo apt update
sudo apt install alsa-utils
sudo apt install sox libsox-fmt-all
```
### 3. Comprobar micrófono
Para identificar a que puerto está conectado el micrófono, ejecuta el siguiente comando:
```bash
arecord -l
```
Se desplegará lo siguiente:

![Terminal](diagramas/terminal.png)

En este caso `card 3` es el puerto al que está conectado el micrófono, por lo tanto al ejecutar el comando para la captura de audio, se deberá definir `plughw:3,0`.

 ### 4. Grabar audio
Para grabar un audio se ejecuta el siguiente comando:
```bash
arecord -D plughw:3,0 -f cd -t wav -d 5 -r 44100 audio.wav
```
Esta instrucción graba 5 segundos, puedes comprobar que todo funciona escuchando el audio que acabas de grabar 

 ### 5. Crear un script para cada función de audio

- [grabar.sh](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/grabar.sh): Graba 15 segundos de audio en calidad CD. 
- [dBmax.sh](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/dBmax.sh): Extrae la amplitud máxima del archivo de audio.
- [dBmin.sh](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/dBmin.sh): Extrae la amplitud mínima del archivo de audio.
- [rms.sh](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/rms.sh): Extrae la amplitud RMS, una medida de la potencia promedio del audio.
- [leer.py](https://github.com/lata-mas/DTHIS_Jorge/blob/main/codigo/leer.py): Lee los datos previamente extraidos y los mando a nuestra plataforma de _IoT_ 

 ### 6. Crear un script ejecutable para correr los otros scripts
Ya que el crontab puede fallar debido a los varios procesos que tiene que realizar, pues todos los realiza al mismo tiempo y puede fallar la _Raspi_. Para eso crearemos un ejecutable _.e_ en el cual pondremos la dirección de los scripts que queremos ejecutar. Primero el de grabar (obvio) en medio los scripts que extraen los datos de sonido y los almaenan en un archivo de texto y al final el script que lee los datos de esos archivos y los manda a nuestro servido de IoT.   

El archivo se crea de la siguiente manera:
```bash
nano ejecutable.e
```

Y su contenido debe ser el siguiente:
```bash
/home/pi/DTHIS/scripts/grabar.sh
/home/pi/DTHIS/scripts/dBmax.sh
/home/pi/DTHIS/scripts/dBmin.sh
/home/pi/DTHIS/scripts/rms.sh
/home/pi/venvs/DTHIS/bin/python3 /home/pi/DTHIS/scripts/leer.py
```
La ultima linea es para activar python dentro del ambiente virtual y así poder correr el script


- ### Cámara
- ### Crontab
