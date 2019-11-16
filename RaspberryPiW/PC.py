import  picamera
from converter_to_base64 import ConverterToBase64
from mqtt_server import  MQTTSenderPicture
from time import sleep,time
from datetime import datetime

class MainCamera():

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.base = ConverterToBase64()
        self.mqttpicture = MQTTSenderPicture()
        self.name = None

    def make_picture(self):
        self.camera.start_preview()
        self.camera.resolution = (1296,972)
        self.name = datetime.now()
        self.camera.capture("{}.jpg".format(self.name))
        self.camera.stop_preview()


    def send_picture(self):
        self.mqttpicture.send_picture("{}.jpg".format(self.name))


    def start_recording(self):
        self.camera.resolution = (1296,972)
        self.name = datetime.now()
        self.camera.start_recording('{}.h264'.format(self.name))
        sleep(10)
        self.camera.stop_recording()
        self.camera.stop_preview()

    def send_video(self):
        self.mqttpicture.send_video("{}.h264".format(self.name))


if __name__ == "__main__":
    mc = MainCamera()
    for _ in range(0,100):
        mc.start_recording()
        mc.send_video()
