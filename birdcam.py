from gpiozero import MotionSensor
from picamera import PiCamera
from uuid import uuid4
from datetime import datetime

camera = PiCamera()
pir = MotionSensor(4)


while True:
    pir.wait_for_motion()
    print("motion detected")
    camera.start_preview()
    # create a unique id for the filename
    filename = './pics/' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_') + str(uuid4()) + '.jpg'
    camera.capture(filename)
    pir.wait_for_no_motion()
    camera.stop_preview()