from picamera import PiCamera
from time import sleep

camera = PiCamera()
keystroke = "a"

sleep(2)
print('starting camera')
camera.start_preview()

while keystroke != "q":
    keystroke = input("press q to quit")
    

camera.stop_preview()
