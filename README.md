# DTHIS

 El dispositivo DTHIS mide las variables de interes dentro del area de diseño bioclimático. En el contexto de la construción de un nuevo edificio para la LIER en el IER, se emplearon estrategias bioclimáticas dentro del mismo y la única manera de comprobar que dichas estrategias funcionan, es a través de los datos que el DTHIS pueda darnos. EL DTHIS (Dispositivo de Temperatura, Humedad, Iluminación y Sonido) funciona con un microprocesador Raspberry Pi y 3 sensores/hardware diferentes, los cuales a través de una seria de códigos recolectan las variables de interes y las mandan a Thingsboard.


## Sensores del DTHIS

| **Sensor**                                    | **Variable**                       | **Cantidad** | **Comunicación** | 
|-----------------------------------------------|------------------------------------|--------------|------------------|
| SCD30 Sensirion                               | Temperatura, CO₂ y Humedad Relativa| 1            | I2C              | 
| Fisheye Camera                                | Luminancia                         | 1            | CSI              |	
| Micrófono ambiental USB                       | dB Maximos, minimos y promedio     | 1            | USB              | 

## Elementos del repositorio
 
- #### En [**CAD**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/CAD) encuentra
	- Planos para 3D

 - #### En [**diagramas**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/diagramas) encuentra
	- Diagrama de conexión

 - #### En [**manual**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/manual) encuentra
	- Manual de operación para recrear el DTHIS

 - #### En [**materiales**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/materiales) encuentra
	- Lista de materiales y costos
        - Fichas técnicas de los sensores y componentes utilizados

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
