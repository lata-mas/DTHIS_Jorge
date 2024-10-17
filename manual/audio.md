# 1. Armado de circuito

En este caso usaremos un microfono USB-C al cual le pusimos un adaptador de C-USB pues la RasPi no tiene mas puertos C

# 2. Descaragar paqueterias necesarias 

```
sudo apt update
sudo apt install alsa-utils
sudo apt install sox libsox-fmt-all
```

# 2. Comprobar que el microfono escucha

Primero se tiene que identificar a que puerto está conectado el micrófono

```
arecord -l
```
Se desplegara algo así:

Los números encerrados son los que se sustituiran en nuestro código



Es muy simple la comporbación, solo tienes que teclrear en la terminal:

```
arecord -D plughw:2,0 -f cd -t wav -d 15 -r 44100
```
El _plughw:2,0_ es la dirección del puerto al que esta conectado nuestro micro, cada RasPi puede decir algo diferente, si funciona correctamente la terminal te dira que esta grabando en ese momento 

# 3. Crear scripts de cada una de las funcicones

Debido a que en este sensor necesitamos que haga mas de una funcion, sugerimos hacer un script por cada una de la funciones que necesitamos para extraer las variables, los scrypts estan en este repositorio, solo tecleas en la terminal:

```
nano
```
Haremos un total de 5 scrypt, uno para escuchar, 1 para cada una de la variables de interes, (Decibeles maximos, minimos y RMS) y el ultimo es para leer los datos extraidos de los otros scrypts y mandarlos al Thingboard. Recuerda terminar tu scrypt con .sh y nombrarlo de una manera que sea sencillo encontrarlo


# 4. Crear un ejecutable para unir todos

```
nano ejecutable.e
```

Debido a que no queremos que nuestra RasPi crashee, haremo un archivo ejecutable .e, en el cual ejecutara todos los scrypts en orden y así no se sobrepongan las instrucciones en la raspi, es importante poner la direccion completa del directorio, al igual que decirle que active el ambiente virtual para correr el scrypt que manda la informacion a ThingsBoard, y queda de la sig manera:

```
./home/pi/DTHIS/grabar30.sh
./home/pi/DTHIS/dBmax.sh
./home/pi/DTHIS/dBmin.sh
./home/pi/DTHIS/rms.sh
.aqui ya no recuerdo como eraaaaa   leer.py
```
# 5. Crontab

Ya que nos interesa que este codigo se ejecute automaticamente cada cierto tiempo usaremos una herramienta para automatizarlo, desde la terminal teclea lo sig:

```
crontab -e
```
Cambiara de interfaz y nos dirigimos hasta la parte final y ponemos lo siguiente :

```
* * * * * /home/pi/DTHIS_jorge/ejecutable.e >> /home/pi/DTHIS_jorge/errores_log.txt 2>&1
```
Lo que le decimos al crontab es que active el ambiente virtual y luego ejecute el codigo en python y mandar los errores a un archivo dado 

Y listo, hay que tomar en cuenta que en el codigo muetra una manera de acceso al Thingsboard cada quien personaliza esa parte, y la manera de comprobar que funciona es que tus datos son enviados correctamente a tu propio Thingsboard










