import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

class MoveDetector():

    def __init__(self):
        pass

    def get_data_from_detector(self):
        GPIO.setmode(GPIO.BCM)
        self.pin = 21
        GPIO.setup(self.pin, GPIO.IN)
        if GPIO.input(self.pin) == True:
            return True
        elif GPIO.input(self.pin) == False:
            return False
        sleep(1)

if __name__ == "__main__":
    md = MoveDetector()
    while True:
        md.print_data_from_detector()