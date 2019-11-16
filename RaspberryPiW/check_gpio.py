import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
pin_list = [21,20,16,12,7,8,25,24,23,18,15,14,2,3,4,17,27,22,10,9,11,5,6,13,19,26]
for pin in pin_list:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.HIGH)
    print(f'Sprawdz czy sie swieci dla GPIO = {pin}')
    input("?")
    GPIO.output(pin, GPIO.LOW)