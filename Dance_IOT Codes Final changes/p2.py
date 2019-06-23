import requests
import json
import paho.mqtt.client as mqtt
import time
import function
# import pygame 

# screen = pygame.display.set_mode((200,200))


i=0
rak=[]
func_object2 = function.function()
start = 0

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
    global start
    #print("Time between messages: ", time.time() - start)
    #start = time.time()

    sensor_data =json.loads(message.payload.decode("utf-8"))
    func_object2.printColours2(sensor_data)

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