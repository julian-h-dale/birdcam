from datetime import datetime
from uuid import uuid4



filename = './pics/' + datetime.now().strftime('%Y_%m_%d_%H_%M_%S_%f_') + str(uuid4()) + '.jpg'
print(filename)