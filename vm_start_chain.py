import paho.mqtt.client as mqtt
import time

RPI_IP = '172.20.10.3'
PORT = 1883

contChainNotConnected = True

def on_connect(client, userdata, flags, rc):
    print("Connected to server with code " + str(rc))

    client.subscribe('fkamal/pong')
    client.message_callback_add('fkamal/pong', on_pong)

def on_pong(client, userdata, message):
    global contChainNotConnected
    contChainNotConnected = False

    time.sleep(1)
    number = int(message.payload)
    number += 1; 

    publish_ping(number)

def publish_ping(data):
    client.publish('fkamal/ping', data)
    print("Publishing ping: " + str(data))

if __name__ == '__main__':
    # Create client obj
    client = mqtt.Client()

    client.on_connect = on_connect

    client.connect(RPI_IP, port = PORT, keepalive = 60)

    client.loop_start()
    time.sleep(1)

    while True:
        if contChainNotConnected == True:
            number = 0
            client.publish('fkamal/ping', number)
            print("Publishing ping: " + str(number))
            time.sleep(4)
        
        time.sleep(1)

