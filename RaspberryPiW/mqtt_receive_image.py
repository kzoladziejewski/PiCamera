"""
File for Aruba Client
"""
import paho.mqtt.client as mqtt
import json, base64, datetime

from DTOinformation import broker, port

class MQTTReceiveImage():

    def __init__(self):
        self.client1= mqtt.Client('ArubaImageCLient')
        self.client1.connect(broker, port)
        self.client1.on_connect = self.on_connect
        self.client1.on_message = self.on_message
        self.client1.subscribe("picture")
        self.client1.on_log = self.on_log
        self.guard = 0
        self.picture_data = []
        while True:
            self.client1.loop_forever()

    @staticmethod
    def on_connect(client, userdata, flags, rc):
        print("Returned code=",rc)

    @staticmethod
    def on_log(client, userdata, level, buf):
        print("log: ", buf)

    def on_message(self,client, userdata, msg):
        unpacked_json = json.loads(msg.payload)
        unpacked_json = unpacked_json.split(",")
        data =unpacked_json[0][11:]
        data = data[:-1]
        pos = int(unpacked_json[3][8:][:-1])
        self.guard+=1
        if self.guard < pos:
            self.picture_data.append(data)
        else:
            self.create_picture(self.picture_data)
            self.guard = 0
            self.picture_data = []

    def create_picture(self, picture):
        picture_data = ' '.join([str(elem) for elem in picture])
        picture_data = picture_data.replace(" ","")
        imgdata = base64.b64decode(picture_data)
        filename = 'test_{}.jpg'.format(datetime.datetime.now())  # I assume you have a way of picking unique filenames
        with open(filename, 'wb') as f:
            f.write(imgdata)


if __name__ == "__main__":
    msp = MQTTReceiveImage()
