from gpiozero import MotionSensor
from picamera import PiCamera
from file_utilities import FilenameGenerator
from file_watcher import Watcher

class BirdCam:
    
    def __init__(self):
        self.camera = PiCamera()
        self.pir = MotionSensor(4)

    def birdWatch(self):
        print("bird cam is watching :)")
        while True:
            self.pir.wait_for_motion()
            print("motion detected")
            filename = FilenameGenerator.generate()
            self.camera.capture(filename)
            self.pir.wait_for_no_motion()


if __name__ == '__main__':
    # start the birdcam
    birdcam = BirdCam()
    birdcam.birdWatch()
    # how to combine with watcher?