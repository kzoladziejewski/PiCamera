import  picamera
import _thread

from mqtt_sender import MQTTSenderPicture
from pir_hc_sr501 import MoveDetector

from time import sleep,time
from datetime import datetime



class MainCamera():

    def __init__(self):
        self.camera = picamera.PiCamera()
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

    def send_notification(self):
        self.mqttpicture.send_information()

if __name__ == "__main__":
    mc = MainCamera()
    md = MoveDetector()
    while True:
        print(md.get_data_from_detector(),datetime.now())
        sleep(1)
        while md.get_data_from_detector():
            mc.send_notification()
            mc.make_picture()
            _thread.start_new_thread(mc.send_picture,())
            mc.start_recording()
            _thread.start_new_thread(mc.send_video,())
