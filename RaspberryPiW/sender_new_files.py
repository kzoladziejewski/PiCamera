"""
Files for Raspberry Pi Zero
"""
import os
import glob
from time import sleep
from mqtt_sender import MQTTSender

class SenderNewFiles():

    def __init__(self):
        self.list_of_image = []
        self.list_of_video = []
        self.mqttserver = MQTTSender()

    def collect_all_files(self):
        for file in glob.glob("*.jpg"):
            self.list_of_image.append(file)
        for file in glob.glob(("*.h264")):
            self.list_of_video.append(file)

    def dispatcher(self):
        for elem in self.list_of_image:
            sleep(2)
            self.mqttserver.send_picture(elem)
            os.remove(elem)
        self.list_of_image = []

        for xa in self.list_of_video:
            sleep(10) #to be sure file is full
            self.mqttserver.send_video(xa)
            os.remove(xa)
        self.list_of_video = []

    def infinity_loop(self):
        while True:
            self.collect_all_files()
            self.dispatcher()

if __name__ == "__main__":
    SNF = SenderNewFiles()
    SNF.infinity_loop()