import RPi.GPIO as GPIO
import cv2
import cv2.aruco as aruco
import threading
from time import sleep
import sys
sys.path.append('/home/pi/pomelo/Main_Lib')
import Side_Lib
from Side_Lib import HizlandirilmisPiKamera
import value

# sudo modprobe bcm2835-v4l2 //this makes picamera visible
from motorClass import Motors

motors = Motors()

class Aruco(Motors):
    def __init__(self):
        self.Motors = motors
        self.camera = HizlandirilmisPiKamera()
        self.camera.veriOkumayaBasla()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create()
        GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print(GPIO.input(37))

    def findAruco(self, q):
        frame = self.camera.veriOku()
        grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedMarkers = aruco.detectMarkers(grayScaleFrame, self.aruco_dict, parameters=self.parameters)[1]

        if detectedMarkers is None or len(detectedMarkers) == 0:
            print("no aruco")
            PressInt = 0
            q.put(PressInt)
                #return PressInt
        else:
            PressInt = 1
            q.put(PressInt)
            
            detectedMarkers = detectedMarkers.tolist()
            commands = []
            
            for i in detectedMarkers:
                commands += i
                print(i)
            self.executeAruco(commands)
            
            #return PressInt
        
        """detectedMarkers = detectedMarkers.tolist()
        commands = []
        
        for i in detectedMarkers:
            commands += i
            print(i)
        self.executeAruco(commands)"""
        
    
    def executeAruco(self, commands): #bu direk olmamış machine code gibi
        duration = 1
        if len(commands) >= 1:
            print(len(commands))
            for i in range(len(commands)):
               
                arucoNumber = commands[i]
                if len(commands) - 1 > i:
                    arucoNumberSecond = commands[i + 1]
                else:
                    arucoNumberSecond = 1
                    print("no specified seconds")
                if arucoNumber == 12:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("back", duration)
                    motors.back(duration)
                if arucoNumber == 11:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("forward", duration)
                    motors.forward(duration)
                if arucoNumber == 14:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                    motors.left(duration)
                if arucoNumber == 13:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("right", duration)
                    motors.right(duration)

    def takeInput(self, q, lock):
        while True:
            lock.acquire()
            #print('hi')
            self.camera.kareyiGoster()
            button = GPIO.input(37)
            if (button == True):
                print("button pressed")
                self.findAruco(q)
                lock.release()
            else:
                lock.release()
