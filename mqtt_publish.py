import time
import random
import paho.mqtt.client as mqtt_client
import sys

mqtt_port=1883
host = ''
topico = ''

def on_publish(client,userdata,result):
    print("data published \n")
    pass

client1= mqtt_client.Client()
client1.on_publish = on_publish
client1.connect(host, mqtt_port)

if len(sys.argv) > 3:
    print('Parametros: host topico timeinterval')
    exit(0)

try:
    host = sys.argv[1]
    topico = sys.argv[2]
    timeinterval = sys.argv[3]
except:
    print('Bad parametters')
    exit(0)


try:
    while True:
        random_value = random.randint(0,70)
        client1.publish(topico, random_value)
        time.sleep(timeinterval)
except KeyboardInterrupt:
    exit(0)
