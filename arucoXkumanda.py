import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as GPIO
import PiWarsTurkiyeRobotKiti2019
#sudo modprobe bcm2835-v4l2 //this makes picamera visible


GPIO.setmode (GPIO.BCM)
GPIO.setup (26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

class Aruco_Controll:
    def __init__(self):
        self.motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()
        self.controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
        self.controller.dinlemeyeBasla()
        self.xy = self.controller.solVerileriOku()
        self.xz = self.controller.sagVerileriOku()
        self.xx = self.controller.butonlariOku()
        self.commands = []
        self.camera = PiWarsTurkiyeRobotKiti2019.HizlandirilmisPiKamera()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create()



    def setup(self):
        self.camera.veriOkumayaBasla()
        self.motors.hizlariAyarla(0, 0)
        print(GPIO.input(26))

    def forward(self, n):
        self.motors.hizlariAyarla(240, 240) #max: 480
        sleep(n)
        self.motors.hizlariAyarla(0, 0)
    def back(self, n):
        self.motors.hizlariAyarla(-240, -240)
        sleep(n)
        self.motors.hizlariAyarla(0, 0)
    def right(self, n):
        self.motors.hizlariAyarla(-240, 240)
        sleep(n)
        self.motors.hizlariAyarla(0, 0)
    def left(self, n):
        self.motors.hizlariAyarla(240, -240)
        sleep(n)
        self.motors.hizlariAyarla(0, 0)

    def takePic(self):
        self.frame = self.camera.veriOku()
        gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
        ids = aruco.detectMarkers(gray, self.aruco_dict, parameters=self.parameters)[1]

        if ids is None or len(ids) == 0:
            print("no aruco")
            return

        ids = ids.tolist()
        self.commands = []
        for i in ids:
            self.commands += i
            print(i)

        #if ids is not None and len(ids) > 0:print(ids.tolist()) #0, 18, 20, 39

    def run(self):
        n = 1
        for i in self.commands:
            if i == 11:
                self.back(n)
                n = 1
            if i == 0:
                self.forward(n)
                n = 1
            if i == 1:
                self.left(n)
                n = 1
            if i == 10:
                self.right(n)
                n = 1
            if i == 9: n = 3

    def takeInput(self):

        while(1):
            if ( GPIO.input(26) == True): #GPIO.input(26) is buttons state when pressed == true
                print("button pressed")
                self.takePic()
                self.run()
            self.Controller()

    def Controller(self):
        while(self.xx != self.controller.butonlariOku() or self.xy != self.controller.sagVerileriOku() or self.xz != self.controller.solVerileriOku()):
            lx, ly = self.controller.solVerileriOku()
            rightSpeed = self.motors.kumandaVerisiniMotorVerilerineCevirme(lx, ly, True)
            leftSpeed = self.motors.kumandaVerisiniMotorVerilerineCevirme(lx, ly, False)
            print(lx," ", ly, " ", rightSpeed, " ", leftSpeed)
            self.motors.hizlariAyarla(rightSpeed, leftSpeed)
            sleep(0.3)
            self.motors.hizlariAyarla(0, 0)
            sleep(0.2)

class Build_Thread:
    def Thread_Monitor(self):
        thread = threading.Thread (target=Aruco.takeInput) #monitör threadi
"""
    def Thread_Aruco_Input(self):
        thread = threading.Thread (target=) #monitör threadi

    def Thread_(self):
        thread = threading.Thread (target=) #monitör threadi
"""


Aruco = Aruco_Controll()
threads = Build_Thread()
Aruco.setup()

