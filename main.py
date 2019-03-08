import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as GPIO
import PiWarsTurkiyeRobotKiti2019
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera


# sudo modprobe bcm2835-v4l2 //this makes picamera visible

class Aruco:
    def __init__(self):
        self.motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol ()
        self.controller = PiWarsTurkiyeRobotKiti2019.Kumanda ()
        self.controller.dinlemeyeBasla ()
        self.xy = self.controller.solVerileriOku ()
        self.xz = self.controller.sagVerileriOku ()
        self.xx = self.controller.butonlariOku ()
        self.commands = []

    def setup(self):
        global camera, aruco_dict, parameters
        self.camera = HizlandirilmisPiKamera ()
        self.camera.veriOkumayaBasla ()
        self.aruco_dict = aruco.Dictionary_get (aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create ()
        self.motors.hizlariAyarla (0, 0)
        GPIO.setmode (GPIO.BCM)
        GPIO.setup (26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(GPIO.input (26))

    def forward(self, duration):
        self.motors.hizlariAyarla (240, 240)  # max: 480
        sleep (duration)
        self.motors.hizlariAyarla (0, 0)

    def back(self, duration):
        self.motors.hizlariAyarla (-240, -240)
        sleep (duration)
        self.motors.hizlariAyarla (0, 0)

    def right(self, duration):
        self.motors.hizlariAyarla (-240, 240)
        sleep (duration)
        self.motors.hizlariAyarla (0, 0)

    def left(self, duration):
        self.motors.hizlariAyarla (240, -240)
        sleep (duration)
        self.motors.hizlariAyarla (0, 0)


"""
    def takePic(self):
        global commands, camera, aruco_dict, parameters
        frame = camera.veriOku ()

        gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)


        ids = aruco.detectMarkers (gray, aruco_dict, parameters=parameters)[1]

        if ids is None or len (ids) == 0:
            print("no aruco")
            return

        ids = ids.tolist ()
        commands = []
        for i in ids:
            commands += i
            print(i)

        # if ids is not None and len(ids) > 0:print(ids.tolist()) #0, 18, 20, 39


    def run(self):
        global commands
        duration = 1
        if len(commands) >=1:
            print(len(commands))
            for i in range(len(commands)):
                print(i)
                arucoNumber = commands[i]
                if len(commands)-1>i:
                    arucoNumberSecond = commands[i+1]
                else:
                    arucoNumberSecond = 1
                    print("no specified seconds")
                if arucoNumber == 12:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("back", duration)
                    self.back (duration)
                if arucoNumber == 11:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("forward", duration)
                    self.forward (duration)
                if arucoNumber == 14:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                    self.left (duration)
                if arucoNumber == 13:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("right", duration)
                    self.right (duration)
                if arucoNumber == 15: duration = 3

"""
    def takeInput(self):
        while (1):
            button_condition = GPIO.input (26)
            if (button_condition == True):
                print("button pressed")
                self.takePic ()
                self.run ()
            while (self.xx != self.controller.butonlariOku () or self.xy != self.controller.sagVerileriOku () or self.xz != self.controller.solVerileriOku ()):
                lx, ly = self.controller.solVerileriOku()
                print(lx, ly)
                rightSpeed, leftSpeed = self.motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly)
                #leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly, False)
                print(lx, " ", ly, " ", rightSpeed, " ", leftSpeed)
                self.motors.hizlariAyarla (rightSpeed, leftSpeed)
                sleep (0.3)
                self.motors.hizlariAyarla (0, 0)
            sleep (0.2)

Aruco_read = Aruco ()
Aruco_read.setup ()

sleep (1)
Aruco_read.forward (1)
thread = threading.Thread (target=Aruco_read.takeInput)
thread.start ()
"""
while (1):

    frame = Aruco_read.camera.veriOku ()
    #camera.kareyiGoster()
   """


