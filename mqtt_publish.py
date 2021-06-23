import time
import random
import paho.mqtt.client as mqtt_client

port=1883

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client1= mqtt_client.Client()
client1.on_publish = on_publish
client1.connect('localhost', port)

try:
    while True:
        random_value = random.randint(0,70)
        client1.publish("facultad/aula8/mota1/temperatura", random_value)
        time.sleep(60)
except KeyboardInterrupt:
    exit(0)