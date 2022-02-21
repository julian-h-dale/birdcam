from gpiozero import MotionSensor
import requests

pir = MotionSensor(4)

if __name__ == '__main__':
    while True:
        pir.wait_for_motion()
        print('motion detcted')
        requests.get('http://localhost:8000/capture')
        pir.wait_for_no_motion()