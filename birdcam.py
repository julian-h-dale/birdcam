from gpiozero import MotionSensor
from picamera import PiCamera
from file_utilities import FilenameGenerator

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
    birdcam = BirdCam()
    birdcam.birdWatch()

# while True:
#     pir.wait_for_motion()
#     print("motion detected")
#     camera.start_preview()
#     # create a unique id for the filename
#     filename = './pics/' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_') + str(uuid4()) + '.jpg'
#     camera.capture(filename)
#     pir.wait_for_no_motion()
#     camera.stop_preview()