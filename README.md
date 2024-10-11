# DTHIS

 El dispositivo DTHIS es crucial para comprobar variables de interes dentro del area de diseño bioclimático. En el contexto de la construción de un nuevo edificio para la LIER en el IER, se emplearon estrategias bioclimáticas dentro del mismo y la única manera de comprobar que dichas estrategias funcionan, es a través de las mediciones que el DTHIS pueda darnos. EL DTHIS (Dispositivo de Temperatura, Humedad, Iluminación y Sonido) funciona con un microprocesador Raspberry Pi y 3 sensores/hardware diferentes, los cuales a través de una seria de códigos recolectan las variables de interes y las mandan a Thingsboard


| **Sensor**                                    | **Variable**                       | **Cantidad** | **Comunicación** | 
|-----------------------------------------------|------------------------------------|--------------|------------------|
| SCD30 Sensirion                               | Temperatura, CO₂ y Humedad Relativa| 1            | I2C              | 
| 5MP OV5647 Wide Angle Fisheye Camera          | Luminancia                         | 1            | CSI              | 			
| Micrófono ambiental USB                       | dB Maximos, minimos y promedio     | 1            | USB              | 
