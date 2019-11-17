"""
File for Raspberry Pi Zero
"""

import  picamera

from time import sleep,time
from datetime import datetime

class MainCamera():

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.name = None

    def make_picture(self):
        self.camera.start_preview()
        self.camera.resolution = (1296,972)
        self.name = datetime.now().strftime("%d%b%Y%H%M%S")
        self.camera.capture("{}.jpg".format(self.name))
        self.camera.stop_preview()

    def start_recording(self):
        self.camera.resolution = (1296,972)
        self.name = datetime.now().strftime("%d%b%Y%H%M%S")
        self.camera.start_recording('{}.h264'.format(self.name))
        sleep(10)
        self.camera.stop_recording()
        self.camera.stop_preview()


    # def send_notification(self):
    #     self.mqttpicture.send_information()

if __name__ == "__main__":
    mc = MainCamera()
    mc.make_picture()
    mc.start_recording()
    # while True:
    #     sleep(1)
    #     while md.get_data_from_detector():
    #         mc.send_notification()
    #         mc.make_picture()
    #         mc.start_recording()
