# DTHIS

 El dispositivo DTHIS es crucial para comprobar variables de interes dentro del area de diseño bioclimático. En el contexto de la construción de un nuevo edificio para la LIER en el IER, se emplearon estrategias bioclimáticas dentro del mismo y la única manera de comprobar que dichas estrategias funcionan, es a través de las mediciones que el DTHIS pueda darnos. EL DTHIS (Dispositivo de Temperatura, Humedad, Iluminación y Sonido) funciona con un microprocesador Raspberry Pi y 3 sensores/hardware diferentes, los cuales a través de una seria de códigos recolectan las variables de interes y las mandan a Thingsboard.


## Sensores del DTHIS

| **Sensor**                                    | **Variable**                       | **Cantidad** | **Comunicación** | 
|-----------------------------------------------|------------------------------------|--------------|------------------|
| SCD30 Sensirion                               | Temperatura, CO₂ y Humedad Relativa| 1            | I2C              | 
| Fisheye Camera                                | Luminancia                         | 1            | CSI              | 			
| Micrófono ambiental USB                       | dB Maximos, minimos y promedio     | 1            | USB              | 

## Elementos del repositorio
 
-  #### En [**CAD**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/CAD) encuentra
	-  Planos para 3D

 - #### En [**Diagramas**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/Diagramas) encuentra
	- Diagrama de conexión

 - #### En [**Manuales**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/Manuales) encuentra
	-  Manual de operación para recrear el DTHIS

 -  #### En [**Materiales**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/Materiales) encuentra
	-  Lista de materiales y costos
        -  Fichas técnicas de los sensores y componentes utilizados

 -  #### En [**Codigo**](https://github.com/lata-mas/DTHIS_Jorge/tree/main/codigo) encuentra
	- Códigos empleados
	- Librerías a utilizar
