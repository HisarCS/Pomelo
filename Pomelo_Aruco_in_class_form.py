import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as GPIO
import PiWarsTurkiyeRobotKiti2019
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera

# sudo modprobe bcm2835-v4l2 //this makes picamera visible


GPIO.setmode (GPIO.BCM)
GPIO.setup (26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
print(GPIO.input (26))


class Aruco():
	def __init__(self):		
		self.motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol ()
		self.motors.hizlariAyarla (0, 0)
		self.controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
		self.controller.dinlemeyeBasla ()
		self.xy = self.controller.solVerileriOku ()
		self.xz = self.controller.sagVerileriOku ()
		self.xx = self.self.controller.butonlariOku ()
		self.commands = []
		self.camera = HizlandirilmisPiKamera()
		self.camera.veriOkumayaBasla()
		self.aruco_dict = aruco.Dictionary_get (aruco.DICT_4X4_250)
	    self.parameters = aruco.DetectorParameters_create ()

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


	def takePic(self, camera):
	    frame = self.camera.veriOku ()

	    gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)
	    

	    ids = aruco.detectMarkers (gray, aruco_dict, parameters=self.parameters)[1]

	    if ids is None or len (ids) == 0:
	        print("no aruco")
	        return

	    ids = ids.tolist ()
	    self.commands = []
	    for i in ids:
	        commands += i
	        print(i)
	    run (self.commands)

    # if ids is not None and len(ids) > 0:print(ids.tolist()) #0, 18, 20, 39


	def run(self, commands):
	    duration = 1
	    if len(self.commands) >=1:
	        print(len(self.commands))
	        for i in range(len(self.commands)):
	            print(i)
	            arucoNumber = self.commands[i] 
	            if len(self.commands)-1>i:
	                arucoNumberSecond = self.commands[i+1]
	            else:
	                arucoNumberSecond = 1
	                print("no specified seconds")
	            if arucoNumber == 12:
	                if arucoNumberSecond <= 10:
	                    duration = arucoNumberSecond 
	                    print ("back", duration)
	                back (duration)  
	            if arucoNumber == 11:
	                if arucoNumberSecond <= 10:
	                    duration = arucoNumberSecond  
	                    print ("forward", duration)
	                forward (duration)
	            if arucoNumber == 14:
	                if arucoNumberSecond <= 10:
	                    duration = arucoNumberSecond  
	                left (duration)
	            if arucoNumber == 13:
	                if arucoNumberSecond <= 10:
	                    duration = arucoNumberSecond  
	                    print ("right", duration)
	                right (duration)
	            if arucoNumber == 15: duration = 3
    


	def takeInput():
	    while (1):
	        y = GPIO.input (26)
	        if (y == True):
	            print("button pressed")
	            takePic (self.camera)
	            
	        while (self.xx != self.controller.butonlariOku () or self.xy != self.controller.sagVerileriOku () or self.xz != self.controller.solVerileriOku ()):
	            lx, ly = self.controller.solVerileriOku ()
	            print(lx, ly)
	            rightSpeed, leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly)
	            #leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly, False)
	            print(lx, " ", ly, " ", rightSpeed, " ", leftSpeed)
	            self.motors.hizlariAyarla (rightSpeed, leftSpeed)
	            sleep (0.3)
	            self.motors.hizlariAyarla (0, 0)

	        sleep (0.2)
Arucuk = Aruco()
Arucuk.setup ()
sleep (1)
thread = threading.Thread (target=Arucuk.takeInput)
thread.start ()

while (1):
    
    frame = Arucuk.camera.veriOku ()
    #camera.kareyiGoster()

