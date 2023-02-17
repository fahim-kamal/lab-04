import paho.mqtt.client as mqtt
import time

RPI_IP = '172.20.10.3'
PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Connected to server with code " + str(rc))

    client.subscribe('fkamal/ping')
    client.message_callback_add('fkamal/ping', on_ping)

def on_ping(client, userdata, message):
    number = int(message.payload)
    number += 1

    publish_pong(number)

def publish_pong(data):
    client.publish('fkamal/pong', data)
    print("Publishing pong: " + str(data))
    time.sleep(1)


if __name__ == '__main__':
    client = mqtt.Client()
    
    client.on_connect = on_connect

    client.connect(RPI_IP, port = PORT, keepalive = 60)

    client.loop_start()
    time.sleep(1)

    while True:
        time.sleep(1)

