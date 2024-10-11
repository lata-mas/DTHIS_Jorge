# 1. Armado del circuito

Para conectar el sensor solo necesitaremos de una Raspi 4 Model B, la mayoria de sensores SCD30 ya vienen con jumpers para conectar direvcto, en caso contrario solamente usar cables jumpers hembra-hembra y conectarlo como el siguiente diagrama

![Diagrama para conectar el sensor SCD30 a la RasPi](https://cdn-learn.adafruit.com/assets/assets/000/100/960/medium640/adafruit_products_SCD30_RasPi_I2C_STEMMA_bb.jpg?1616617527)

# 2. Habilitar comunicación 12C

Para activar la comunicacion 12C debemos activarla desde la terminal de la RasPi y hacer lo siguiente

```ruby
sudo raspi-config
```
1. Una vez ahí tenemos que dirigirnos a la parte de Interface Options
2. Seleecionamos 12C
3. Confirmamos la habilitación en la terminal
4. Debes reiniciar la RasPi



# 3. Creación de un ambiente virtual

Para esta parte es importante recordar tener un espacio de trabajo organizado, vamos a crear una carpeta en la cual contendra nuestro ambiente virtual, asegurate de llamar a tu ambiente con un nombre relacionado, en este caso el mismo nombre que el sensor.

```ruby
mkdir ambientes
cd ambientes
python -m venv SCD30
```
Una vez creado procedemos a activarlo con el siguiente comando
```ruby
source SCD30/bin/activate
(SCD30) $
```
Si el nombre de tu ambiente aparece en paréntesis antes del signo $ es que se activó correctamente


# 4. Descargar paqueterias necesarias

Para esta parte solo vastara con ejecutar 2 lineas, importa mencionar que la creación del ambiente virtual es necesario para la descarga de estas paqueteria, ya que la RaspberyPi ya viene con paqueterias de facto, y para no afectar a la misma Raspberry se requiere crear el ambiente para sobre de el trabajar. Entonces:
```
pip3 install w1thermsensor
pip3 install paho-mqtt
```

# 5. Codigo

Ahora vamos a crear un script con el código poniendo el siguiente comando en la terminal:
```
nano
```
Utiliza el codigo anexado a este repositorio, despues _ctrl + O_ para guardar, te dice que asignes un nombre, recuerda que termina con .py y por ultimo _ctrl + X_ para salir.

# 6. Habilitar crontab

Ya que nos interesa que este codigo se ejecute automaticamente cada cierto tiempo usaremos una herramienta para automatizarlo, desde la terminal teclea lo sig:

```
crontab -e
```
Cambiara de interfaz y nos dirigimos hasta la parte final y ponemos lo siguiente :

```
*/2 * * * * /bin/bash -c 'source /home/pi/SCD30/bin/activate && /home/pi/SCD30/bin/python3 /home/pi/DTHIS_jorge/t_hr_co2.py' >> /home/pi/DTHIS_jorge/t_hr_co2.log 2>&1
```
Lo que le decimos al crontab es que active el ambiente virtual y luego ejecute el codigo en python y mandar los errores a un archivo dado 

Y listo, hay que tomar en cuenta que en el codigo muetra una manera de acceso al Thingsboard cada quien personaliza esa parte, y la manera de comprobar que funciona es que tus datos son enviados correctamente a tu propio Thingsboard





