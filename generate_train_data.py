from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.rotation = 90

camera.start_preview()
for i in range(400,500):
    camera.capture('/home/pi/Documents/GitHub/Cat-Classifier/data/base/image%s.jpg' % i)
    print("image%s.jpg fertig" % i)
    sleep(1)
camera.stop_preview()
