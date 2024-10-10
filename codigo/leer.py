import time
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'tb.ier.unam.mx'
UNIQUE_ID = 'f1bd5cf0-2754-11ef-ac1b-fb0c99e98d63' 
ACCESS_TOKEN = '5s444k8d0vkUmBQtGKd3'

archivos = ['/home/pi/DTHIS_jorge/rms.txt', '/home/pi/DTHIS_jorge/dBmax.txt', '/home/pi/DTHIS_jorge/dBmin.txt']
rms_x  = ""
dBmax_x = ""
dBmin_x = ""

for archivo in archivos:
    with open(archivo, 'r', encoding='utf-8') as f:
        if archivo == '/home/pi/DTHIS_jorge/rms.txt':
            rms_x = f.read().strip()
        elif archivo == '/home/pi/DTHIS_jorge/dBmax.txt':
            dBmax_x = f.read().strip()
        elif archivo == '/home/pi/DTHIS_jorge/dBmin.txt':
            dBmin_x = f.read().strip()

micro_data = {'RMS': rms_x,'dBmax': dBmax_x,'dBmin': dBmin_x}

client = mqtt.Client(UNIQUE_ID, False)
client.username_pw_set(ACCESS_TOKEN, password=None)

client.connect(THINGSBOARD_HOST, 1883, 60, "")
client.loop_start()
time.sleep(2)
try:
    client.publish('v1/devices/me/telemetry', json.dumps(micro_data))
    print(f"  RMS {micro_data['RMS']}\n", f" Decibeles maximos {micro_data['dBmax']}\n", f" Decibeles minimos {micro_data['dBmin']}\n")
except KeyboardInterrupt:
    pass

client.loop_stop()
client.disconnect()
