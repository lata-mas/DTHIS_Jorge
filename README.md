# DTHIS

 El dispositivo DTHIS mide las variables de interes dentro del area de diseño bioclimático. En el contexto de la construción de un nuevo edificio para la LIER en el IER, se emplearon estrategias bioclimáticas dentro del mismo y la única manera de comprobar que dichas estrategias funcionan, es a través de los datos que el DTHIS pueda darnos. EL DTHIS (Dispositivo de Temperatura, Humedad, Iluminación y Sonido) funciona con un microprocesador Raspberry Pi y 3 sensores/hardware diferentes, los cuales a través de una seria de códigos recolectan las variables de interes y las mandan a una plataforma de internet de las cosas como  Thingsboard.


## Sensores del DTHIS

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
	- Planos para 3D

 - #### En [**diagramas**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/diagramas) encuentra
	- Diagrama de conexión

 - #### En [**manual**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/manual) encuentra
	- Manual de operación para recrear el DTHIS

 - #### En [**codigo**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/codigo) encuentra
	- Códigos empleados
	- Librerías a utilizar

## Elaboracion 

- ### Iniciar Raspberry
	- El primer paso es habilitar el microprocesador Raspberry Pi 4 Model B, para ellos necesitaremos una memoria Micro SD de 64 Gb para descargar desde cualquier ordenador el sistema operativo. Una vez lista la SD se inserta en la _Raspi_ e instalamos el sistema operativo en la maquina.

- ### Ensamblado de sensores




- ### SCD30 
- ### Micrófono 
- ### Cámara
- ### 
