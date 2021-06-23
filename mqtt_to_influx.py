from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt_client
import json

def connect(client, userdata, flags, rc):
    client.subscribe("facultad/aula8/mota1/temperatura")

def on_message(client, userdata, msg):
    topic = msg.topic
    message_decoded=str(msg.payload.decode("utf-8", "ignore"))
    value = json.loads(message_decoded)
    print(value)
    json_body = [
        {
            "measurement": "temperatura",
            "tags":{
                "localidad": "La Plata",
            },
            "fields":{
                "value":float(value),
            }
        }
    ]
    client_influxdb.write_points(json_body)

def influx_connect():
    client_influxdb = InfluxDBClient(host='localhost', port=8086, database='database1')
    return client_influxdb

def mqtt_connect():
    cliente_mqtt = mqtt_client.Client()
    cliente_mqtt.on_connect = connect
    cliente_mqtt.on_message = on_message
    cliente_mqtt.connect('localhost', 1883, 60)
    return cliente_mqtt


cliente_mqtt = mqtt_connect()
client_influxdb = influx_connect()
try:
    cliente_mqtt.loop_forever()
except KeyboardInterrupt:
    exit(0)