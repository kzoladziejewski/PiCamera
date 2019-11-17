"""
File for Raspberry Pi Zero
"""
from time import sleep
from pir_hc_sr501 import MoveDetector
from PC import MainCamera

class HomeMonitoring():
    def __init__(self):
        print("WELCOME TO HOME MONITORING BY KACPER ZOLADZIEJEWSKI")
        print("YOUR HAPPY IS MY HAPPY")
        self.md = MoveDetector()
        self.camera = MainCamera()

    def main_home_monitoring(self):
        while True:
            sleep(1)
            while self.md.get_data_from_detector():
                self.camera.make_picture()
                self.camera.start_recording()

if __name__ == "__main__":
    HM = HomeMonitoring()
    HM.main_home_monitoring()