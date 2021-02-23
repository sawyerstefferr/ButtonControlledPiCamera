from picamera import PiCamera
from time import sleep
from gpiozero import Button
import datetime

camera = PiCamera()

def cam_function():
    datetime_current = datetime.datetime.now()
    timestamp = datetime_current.timestamp()
    camera.start_preview(alpha=200)
    # for i in range(5):
    #     sleep(5)
    #     camera.capture('/home/pi/Desktop/image%s.jpg' %i)
    sleep(5)
    camera.capture('/home/pi/Desktop/%s.jpg' %timestamp)
    camera.annotate_text = "%s" % datetime_current
    camera.stop_preview()
    
button_camera = Button(4)
button_camera.when_pressed=cam_function()



