import time
import board
import busio
from scd30_i2c import SCD30
import paho.mqtt.client as mqtt
import json

scd30 = SCD30()

CO2, T, HR = scd30.read_measurement()


THINGSBOARD_HOST = 'tb.ier.unam.mx'
UNIQUE_ID = 'f1bd5cf0-2754-11ef-ac1b-fb0c99e98d63' 
ACCESS_TOKEN = '5s444k8d0vkUmBQtGKd3'

sensor_data = {'T': 0,'HR': 0, 'CO2': 0} 
client = mqtt.Client(UNIQUE_ID, False)
client.username_pw_set(ACCESS_TOKEN, password=None)

client.connect(THINGSBOARD_HOST, 1883, 60, "")
client.loop_start()
time.sleep(2)
try:
    
    while True:
        
        if scd30.get_data_ready():
            CO2, T, HR = scd30.read_measurement()
                  
        sensor_data['T']      = T
        sensor_data['HR']     = HR
        sensor_data['CO2']    = CO2
        client.publish('v1/devices/me/telemetry', json.dumps(sensor_data))
        print(f"Temperatura {sensor_data['T']} °c\n",
              f"{sensor_data['HR']}% de Humedad\n",
              f"Nivel de CO2 {sensor_data['CO2']}\n")
        break       

except KeyboardInterrupt:
    pass



client.loop_stop()
client.disconnect()
