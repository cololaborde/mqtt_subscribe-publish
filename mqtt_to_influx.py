from influxdb import InfluxDBClient
import paho.mqtt.client as mqtt_client
import json
import sys

host = ''
topico = ''
database = ''
influx_port = 8086
mqtt_port = 1883

def connect(client, userdata, flags, rc):
    client.subscribe(topico)

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
    client_influxdb = InfluxDBClient(host=host, port=influx_port, database=database)
    return client_influxdb

def mqtt_connect():
    cliente_mqtt = mqtt_client.Client()
    cliente_mqtt.on_connect = connect
    cliente_mqtt.on_message = on_message
    cliente_mqtt.connect(host, mqtt_port, 60)
    return cliente_mqtt


if len(sys.argv) < 4:
    print('Parametros: host topico database')
    exit(0)

try:
    host = sys.argv[1]
    topico = sys.argv[2]
    database = sys.argv[3]
except:
    print('Bad parametters')
    exit(0)



cliente_mqtt = mqtt_connect()
client_influxdb = influx_connect()
try:
    cliente_mqtt.loop_forever()
except KeyboardInterrupt:
    exit(0)
