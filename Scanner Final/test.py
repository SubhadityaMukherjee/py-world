from SimpleCV import JpegStreamCamera, Display
import time

disp = Display()

address = 'http://admin:1234@192.168.0.106:8081'
print address
cam = JpegStreamCamera(address)

while disp.isNotDone():
    img = cam.getImage()
    img.save(disp)
    time.sleep(1)
