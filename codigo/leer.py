import time
import paho.mqtt.client as mqtt
import json

THINGSBOARD_HOST = 'tb.ier.unam.mx'
UNIQUE_ID = '58674640-fae6-11ef-b37b-add9be6ef0f3' #4 5f3b2b30-fae6-11ef-b37b-add9be6ef0f3  #5 64e7f540-fae6-11ef-b37b-add9be6ef0f3  #6 6abb8130-fae6-11ef-b37b-add9be6ef0f3 #7 704b2650-fae6-11ef-b37b-add9be6ef0f3  #8 76b992b0-fae6-11ef-b37b-add9be6ef0f3
ACCESS_TOKEN = 'Bu3KK4ZWjkM9sRRGi3F8' #4 2fn5wQSDRcAfzXpihGG5  #5 L1OPtuo9ASQsf2bF2V2f #6 zM1N1sE6GbIjvu5EwmWq  #7 nAxgM43HZ9SrM5Fqlg2X  #8 oOsXYqvmmeYrNUJOOq1R

archivos = ['/home/pi/DTHIS/txt/rms.txt', '/home/pi/DTHIS/txt/dBmax.txt', '/home/pi/DTHIS/txt/dBmin.txt']
rms_x  = ""
dBmax_x = ""
dBmin_x = ""

for archivo in archivos:
    with open(archivo, 'r', encoding='utf-8') as f:
        if archivo == '/home/pi/DTHIS/txt/rms.txt':
            rms_x = f.read().strip()
        elif archivo == '/home/pi/DTHIS/txt/dBmax.txt':
            dBmax_x = f.read().strip()
        elif archivo == '/home/pi/DTHIS/txt/dBmin.txt':
            dBmin_x = f.read().strip()

rms_db = 20 * np.log10(float(rms_x)) + 120
dBmax_db = 20 * np.log10(float(dBmax_x)) + 120
dBmin_db = 20 * np.log10(abs(float(dBmin_x))) + 120 

micro_data = {'RMS': rms_db,'dBmax': dBmax_db,'dBmin': dBmin_db}

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
