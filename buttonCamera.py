from picamera import PiCamera
from time import sleep
from gpiozero import Button

#with PiCamera() as camera:
#    camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
#    camera.resoultion = (640, 480)
#    button.wait_for_press()
#    camera.capture('./resources/test.jpg')
#    camera.stop_preview()


class Camera: 
    def __init__(self, DIR_PATH, FILE_NAME):
       self.DIR_PATH = DIR_PATH
       self.FILE_NAME = FILE_NAME
       self.button = Button(21)
    
    def getPicture(self):
        camera = PiCamera()
        camera.start_preview()
        #camera.resolution = (1024, 768)
        #camera.start_preview(fullscreen=False, window=(100, 20, 640, 480))
        self.button.wait_for_press()
        camera.capture(self.DIR_PATH + '/' + self.FILE_NAME)
        camera.stop_preview()

    def run(self):
        self.getPicture()
    
    def getBtn(self):
        return self.button
