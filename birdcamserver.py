import hug
from file_utilities import FilenameGenerator
from picamera import PiCamera



@hug.local()

@hug.get('/test_focus', output=hug.output_format.jpg_image)
def test_focus():
    camera = PiCamera()
    camera.capture('./pics/testfocus.jpg')
    camera.close()
    return './pics/testfocus.jpg'

@hug.get('/capture')
def capture():
    camera = PiCamera()
    filename = FilenameGenerator.generate()
    camera.capture(filename)
    camera.close()
    return {'image': filename}