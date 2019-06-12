import requests
import json
import paho.mqtt.client as mqtt
import time


i=0
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("biosense/Sensor_test_R/data")
    client.subscribe("biosense/Sensor_test_L/data")
    client.subscribe("biosense/Sensor_test_H/data")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, message):
    # if client.flag==0:
    client.rak.append(message.payload.decode("utf-8")) 
    client.newrak.append(message.payload.decode("utf-8"))
    # elif client.flag==1:
    #     client.rakL.append(message.payload.decode("utf-8"))
    # else:
    #     client.rakH.append(message.payload.decode("utf-8"))  
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

    # client.flag+=1
    # if client.flag==3:
    #     client.flag=0
#def on_message(client, userdata, msg):
  # print(i)
  # i=i+1

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.iglor.es", 8080, 60)
start = time.time()
client.loop_start()
end = time.time()
print(end - start)
while True:
	time.sleep(5)
#	print('connected...')