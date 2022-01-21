import hug
from file_utilities import FilenameGenerator
from picamera import PiCamera
import glob

# not completely convinced this singledton implementation works
# nor that its a good idea 
# but the error of having multiple calls break the camera has been fixed
class CameraSingleton():
    def __init__(self):
        print('camera init called')
        self.camera = PiCamera()

    def instance(self):
        if  self.camera:
            return self.camera

cameraContainer = CameraSingleton()

@hug.local()
@hug.get('/test_focus', output=hug.output_format.jpg_image)
def test_focus():
    cameraContainer.instance().capture('./pics/testfocus.jpg')
    return './pics/testfocus.jpg'

@hug.get('/capture')
def capture():
    filename = FilenameGenerator.generate()
    cameraContainer.instance().capture(filename)
    return {'image': filename}

@hug.get('/pics')
def get_pics():
    fileList = [f for f in glob.glob('./pics/*.jpg')]
    picList = []
    for pic in fileList:
        picList.append({'url': pic, 'filename': pic.split('/')[-1], 'id': pic.split('/')[-1].split('_')[-1]})
    return picList

@hug.get('/pic', examples='pic=20021-23121.jpg', output=hug.output_format.jpg_image)
def get_pic(pic: hug.types.text):
    return './pics/' + pic