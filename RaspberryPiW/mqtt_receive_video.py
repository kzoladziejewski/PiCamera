import paho.mqtt.client as mqtt
from time import sleep
import json, random
import base64,datetime
from subprocess import CalledProcessError
import subprocess

class MQTTSenderPicture():

    def __init__(self):
        self.broker="80.211.195.240"
        self.port=1883
        self.client1= mqtt.Client('a')
        self.client1.connect(self.broker,self.port)
        self.client1.on_connect = self.on_connect
        self.client1.on_log = self.on_log
        self.client1.on_message = self.on_message
        self.client1.subscribe("testowy_video")
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
            self.create_video(self.picture_data)
            self.guard = 0
            self.picture_data = []

    def create_video(self, picture):

        picture_data = ' '.join([str(elem) for elem in picture])
        picture_data = picture_data.replace(" ","")
        imgdata = base64.b64decode(picture_data)
        name = datetime.datetime.now().strftime("%d%b%Y%H%M%S")
        filename = 'test_{}.h264'.format(name)  # I assume you have a way of picking unique filenames

        with open(filename, 'wb') as f:
            f.write(imgdata)

        command = "MP4Box -add {} {}.mp4".format(filename,name)
        try:
            output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
        except subprocess.CalledProcessError as e:
            print('FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))


if __name__ == "__main__":
    msp = MQTTSenderPicture()
