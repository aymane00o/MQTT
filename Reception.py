import paho.mqtt.client as mqtt
from random import randrange , uniform
import time
def on_message(client,userdata,message):
    print("Hana message: ",str(message.payload.decode("latin-1")))
    
mqttBroker = "192.168.61.246"
client = mqtt.Client("v1")
client.connect(mqttBroker)
client.loop_start()
client.subscribe("v2v") #v2v is the topic 
client.on_message = on_message
time.sleep(30)
client.loop_end()
