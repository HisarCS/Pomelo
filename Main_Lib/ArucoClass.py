"""import RPi.GPIO as GPIO
import cv2
import cv2.aruco as aruco
import threading
from time import sleep

import Side_Lib
from Side_Lib import HizlandirilmisPiKamera

# sudo modprobe bcm2835-v4l2 //this makes picamera visible
from motorClass import Motors
"""

class Aruco():
    """def __init__(self, Motors):
        self.Motors = Motors
        self.controller = Side_Lib.Kumanda()
        self.controller.dinlemeyeBasla()
        self.xy = self.controller.solVerileriOku()
        self.xz = self.controller.sagVerileriOku()
        self.xx = self.controller.butonlariOku()
        self.camera = HizlandirilmisPiKamera()
        self.camera.veriOkumayaBasla()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create()
        GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print(GPIO.input(26))

    def findAruco(self):
        frame = self.camera.veriOku()
        grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedMarkers = aruco.detectMarkers(grayScaleFrame, self.aruco_dict, parameters=self.parameters)[1]

        if detectedMarkers is None or len(detectedMarkers) == 0:
            print("no aruco")
            return

        detectedMarkers = detectedMarkers.tolist()
        commands = []
        for i in detectedMarkers:
            commands += i
            print(i)
        self.executeAruco(commands)

    # if detectedMarkers is not None and len(detectedMarkers) > 0:print(detectedMarkers.tolist()) #0, 18, 20, 39

    def executeAruco(self, commands): #bu direk olmamış machine code gibi
        duration = 1
        if len(commands) >= 1:
            print(len(commands))
            for i in range(len(commands)):
                print(i)
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
                    self.Motors.back(duration)
                if arucoNumber == 11:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("forward", duration)
                    self.Motors.forward(duration)
                if arucoNumber == 14:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                    self.Motors.left(duration)
                if arucoNumber == 13:
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        print ("right", duration)
                    self.Motors.right(duration)"""

    def takeInput(self):
        while True:
            print("button pressed")
