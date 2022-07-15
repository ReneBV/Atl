import paho.mqtt.client as mqtt
import time

token = 'Y7ZcpMp0cEkcUE5jYU43'
broker = "demo.thingsboard.io"
port = 8080
topic = "v1/devices/me/telemetry"

def on_connect(client, userdata, flags, rc):
    if (rc == 0):
        print("connected OK returned code = ", rc)
    else:
        print("Bad connection returned code = ", rc)

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(token)
client.connect(broker, port, 60)
client.subscribe(topic)

client.loop_forever()
