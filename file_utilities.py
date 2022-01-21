from datetime import datetime
from uuid import uuid4

class FilenameGenerator:
    FILE_DIRECTORY = './pics/'
    FILE_TAG = '.jpg'

    @staticmethod
    def generate():
        return FilenameGenerator.FILE_DIRECTORY + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_') + str(uuid4()) + FilenameGenerator.FILE_TAG

if __name__ == '__main__':
    print(FilenameGenerator.generate())