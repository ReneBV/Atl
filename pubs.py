import paho.mqtt.client as paho
import os
import json
import time
from datetime import datetime
from random import randint

ACCESS_TOKEN = 'Y7ZcpMp0cEkcUE5jYU43'
broker = 'demo.thingsboard.io'
port = 1883

def on_publish(client,userdata,result):
    print("data published to thingsboard \n")
    pass
client1 = paho.Client("D1")
client1.on_publish = on_publish
client1.username_pw_set(ACCESS_TOKEN)
client1.connect(broker, port, keepalive=60)

while True:
    hum_val = randint(50, 120)
    temp_val = randint(75, 150)
    payload = "{"
    payload += "\"Humidity\":"+str(hum_val)+",";
    payload += "\"Temperature\":"+str(temp_val);
    payload += "}"
    ret = client1.publish("v1/devices/me/telemetry", payload)
    print("Please check LASTEST TELEMETRY field of your device")
    print(payload)
    time.sleep(5)