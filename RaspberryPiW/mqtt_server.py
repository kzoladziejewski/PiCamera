import paho.mqtt.client as mqtt
import json
import base64
import math
from random import randint
class MQTTSenderPicture():

    def __init__(self):
        self.broker="80.211.195.240"
        self.port=1883
        self.client1= mqtt.Client("control1")                           #create client object
        self.client1.on_publish = self.on_publish
        self.client1.connect(self.broker,self.port)                                 #establish connection
        # self.client1.on_log = self.on_log
        self.packet_size=3000

    def on_publish(self, client, userdata, resultt):
        # print("Picure send")
        pass
    def on_log(self,client, userdata, level, buf):
        print("log: ", buf)

    def convertImageToBase64(self, picture):
        with open("{}".format(picture), "rb") as image_file:
            encoded = base64.b64encode(image_file.read())
        return encoded

    def publishEncodedImage(self, encoded, topic):
        end = self.packet_size
        start = 0
        length = len(encoded)
        picId = "dupa"
        pos = 0
        no_of_packets = math.ceil(length / self.packet_size)

        while start <= len(encoded):
            data = {"data": encoded[start:end], "pic_id": picId, "pos": pos, "size": no_of_packets}
            # self.client1.publish("testowy", json.JSONEncoder().encode(data))
            self.client1.publish(topic, json.dumps(str(data)))
            end += self.packet_size
            start += self.packet_size
            pos = pos + 1


    def send_picture(self, picture):
        self.publishEncodedImage(self.convertImageToBase64(picture), 'testowy')

    def send_video(self, video):
        self.publishEncodedImage(self.convertImageToBase64(video), "testowy_video")
                        #assign function to callback
        # ret= client1.publish("testowy",json.JSONEncoder().encode(picture))                   #publish
        # message = '"image": {"bytearray":"' + str(byte) + '"} } '
        # self.client1.publish("testowy","{}".format(randint(0,125)))
        # self.client1.publish("testowy",payload=message, qos=1, retain=False)                   #publish
