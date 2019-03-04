import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as GPIO
import PiWarsTurkiyeRobotKiti2019
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera

# sudo modprobe bcm2835-v4l2 //this makes picamera visible


motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol ()
controller = PiWarsTurkiyeRobotKiti2019.Kumanda ()
controller.dinlemeyeBasla ()
xy = controller.solVerileriOku ()
xz = controller.sagVerileriOku ()
xx = controller.butonlariOku ()
commands = []


def setup():
    global camera, aruco_dict, parameters
    camera = HizlandirilmisPiKamera ()
    camera.veriOkumayaBasla ()
    aruco_dict = aruco.Dictionary_get (aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create ()
    motors.hizlariAyarla (0, 0)
    GPIO.setmode (GPIO.BCM)
    GPIO.setup (26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    print(GPIO.input (26))


def forward(duration):
    motors.hizlariAyarla (240, 240)  # max: 480
    sleep (duration)
    motors.hizlariAyarla (0, 0)


def back(duration):
    motors.hizlariAyarla (-240, -240)
    sleep (duration)
    motors.hizlariAyarla (0, 0)


def right(duration):
    motors.hizlariAyarla (-240, 240)
    sleep (duration)
    motors.hizlariAyarla (0, 0)


def left(duration):
    motors.hizlariAyarla (240, -240)
    sleep (duration)
    motors.hizlariAyarla (0, 0)


def takePic():
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


def run():
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
            takePic ()
            
            run ()
        while (
                xx != controller.butonlariOku () or xy != controller.sagVerileriOku () or xz != controller.solVerileriOku ()):
            lx, ly = controller.solVerileriOku ()
            print(lx, ly)
            rightSpeed, leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly)
            #leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly, False)
            print(lx, " ", ly, " ", rightSpeed, " ", leftSpeed)
            motors.hizlariAyarla (rightSpeed, leftSpeed)
            sleep (0.3)
            motors.hizlariAyarla (0, 0)

        sleep (0.2)


setup ()

sleep (1)
thread = threading.Thread (target=takeInput)
thread.start ()

while (1):
    
    frame = camera.veriOku ()
    camera.kareyiGoster()
   
