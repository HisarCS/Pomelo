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

from motorClass import Motors

motors = Motors()

class Aruco(Motors): #Creates the class for Aruco Block detection 
    def __init__(self): #Initializes required objects and variables
        self.Motors = motors
        self.camera = HizlandirilmisPiKamera()
        self.camera.veriOkumayaBasla()
        self.aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
        self.parameters = aruco.DetectorParameters_create()
        self.input_list = []
        GPIO.setup(37, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        print(GPIO.input(37))

    def findAruco(self, q, q2): #Method for scanning the Aruco Codes in the picture taken by pressing the button
        frame = self.camera.veriOku()
        #Make the screen grayscale for easier readability..
        grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        detectedMarkers = aruco.detectMarkers(grayScaleFrame, self.aruco_dict, parameters=self.parameters)[1]

        if detectedMarkers is None or len(detectedMarkers) == 0: #Check if there are any Aruco Codes present
            print("no aruco")
            PressInt = 0
            q.put(PressInt) #Give value to the thread so that it can use the appropriate monitor reaction.
                
        else:
            PressInt = 1
            q.put(PressInt)
            
            detectedMarkers = detectedMarkers.tolist()
            commands = []
            #Add the value of each Aruco Marker scanned to a list.
            for i in detectedMarkers:
                commands += i
                print(i)
            self.executeAruco(commands, q2) #Use the list of commands and exetuce them using the method
        
    
    def executeAruco(self, commands, q2): #Method for executing commands based on the value of the scanned Aruco Marker
        duration = 1
        if len(commands) >= 1:
            print(len(commands))
            for i in range(len(commands)): #Fore every Aruco scanned
               
                arucoNumber = commands[i]
                if len(commands) - 1 > i:#If the Aruco value is <= 10 then use it as a timer for the next action.
                    arucoNumberSecond = commands[i + 1]
                    self.input_list.append(arucoNumberSecond)
                else:
                    arucoNumberSecond = 1
                    print("no specified seconds")
                if arucoNumber == 12: #Go backwards for specified amounts of seconds.
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        aruco_func = "back " + str(duration)
                        print (aruco_func)
                        self.input_list.append(aruco_func) #Add used command to inputs lits (Used for website data)
                    motors.back(duration)
                if arucoNumber == 11: #Go forwards for specified amounts of seconds.
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        aruco_func = "forward " + str(duration)
                        print (aruco_func)
                        self.input_list.append(aruco_func)
                    motors.forward(duration)
                if arucoNumber == 14: #Go left for specified amounts of seconds.
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        aruco_func = "left " + str(duration)
                        print (aruco_func)
                        self.input_list.append(aruco_func)
                    motors.left(duration)
                if arucoNumber == 13: #Go right for specified amounts of seconds.
                    if arucoNumberSecond <= 10:
                        duration = arucoNumberSecond
                        aruco_func = "right " + str(duration)
                        print (aruco_func)
                        self.input_list.append(aruco_func)
                    motors.right(duration)
            q2.put(input_list)
    def takeInput(self, q, q2, q3, lock):
        while True:
            lock.acquire() #Lock the monitor thread so they wont clash.
            button_press = 0
            self.camera.kareyiGoster()
            button = GPIO.input(37)#Open button for input
            self.input_list = []#Re-Initialize input list (Used for website)
            if (button == True):
                print("button pressed")
                button_press += 1
                q3.put(button_press)
                self.findAruco(q, q2) #Start method with the queue value used to determine the emote in monitor.
                lock.release() #Release lock for monitor thread.
            else:
                lock.release()