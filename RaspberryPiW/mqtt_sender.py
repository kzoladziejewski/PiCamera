"""
File for Raspberry Pi Zero
"""
import paho.mqtt.client as mqtt
import json
import base64
import math

from DTOinformation import broker, port

class MQTTSender():

    def __init__(self):

        self.client1= mqtt.Client("RaspberryPi")                           #create client object
        self.client1.on_publish = self.on_publish
        self.client1.connect(broker,port)                                 #establish connection
        self.client1.on_log = self.on_log
        self.packet_size=3000

    def on_publish(self, client, userdata, resultt):
        pass

    def on_log(self,client, userdata, level, buf):
        print("log: ", buf)

    def convertImageToBase64(self, picture):
        with open("{}".format(picture), "rb") as image_file:
            encoded = base64.b64encode(image_file.read())
        return encoded

    def publishEncodedData(self, encoded, topic):
        end = self.packet_size
        start = 0
        length = len(encoded)
        pos = 0
        no_of_packets = math.ceil(length / self.packet_size)
        picId = "picId"
        while start <= len(encoded):
            data = {"data": encoded[start:end], "pic_id": picId, "pos": pos, "size": no_of_packets}
            self.client1.publish(topic, json.dumps(str(data)))
            end += self.packet_size
            start += self.packet_size
            pos = pos + 1

    @staticmethod
    def on_log(client, userdata, level, buf):
        print("log: ", buf)

    def send_picture(self, picture):
        self.publishEncodedData(self.convertImageToBase64(picture), 'picture')

    def send_video(self, video):
        self.publishEncodedData(self.convertImageToBase64(video), "video")

    def send_information(self):
        data = {"data": "Detect move!"}
        self.client1.publish("move",json.dumps((str(data))))
