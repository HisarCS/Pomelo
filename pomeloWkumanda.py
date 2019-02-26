import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as g
import PiWarsTurkiyeRobotKiti2019
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
#sudo modprobe bcm2835-v4l2 //this makes picamera visible

commands = []

motors = PiWarsTurkiyeRobotKiti2019.MotorKontrol()

controller = PiWarsTurkiyeRobotKiti2019.Kumanda()
controller.dinlemeyeBasla()
xy = controller.verileriOku()
def setup():
    global camera, aruco_dict, parameters
    camera = HizlandirilmisPiKamera()
    camera.veriOkumayaBasla()
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create()
    motors.setSpeeds(0, 0)
    g.setmode(g.BCM)
    g.setup(26, g.IN, pull_up_down=g.PUD_DOWN)
    print(g.input(26))

def forward(n):
    motors.setSpeeds(240, 240) #max: 480
    sleep(n)
    motors.setSpeeds(0, 0)

def back(n):
    motors.setSpeeds(-240, -240)
    sleep(n)
    motors.setSpeeds(0, 0)
    
def takePic():
    global commands, camera, aruco_dict, parameters
    frame = camera.veriOku()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ids = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)[1]

    if ids is None or len(ids) == 0:
        print("no aruco")
        return
    
    ids = ids.tolist()
    commands = []
    for i in ids:
        commands += i
        print(i)
        
    #if ids is not None and len(ids) > 0:print(ids.tolist()) #0, 18, 20, 39

def run():
    global commands
    n = 1
    for i in commands:
        if i == 12:
            back(n)
            n = 1
        if i == 13:
            forward(n)
            n = 1
        if i == 9: n = 3

def takeInput():
    while(1):
        print("ey")
        takePic()
        run()
        sleep(0.2)
    

setup()
sleep(1)
thread = threading.Thread(target=takeInput)
thread.start()
while(1):
    frame = camera.veriOku()
    sleep(0.05)
import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
import RPi.GPIO as g
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
#sudo modprobe bcm2835-v4l2 //this makes picamera visible

commands = []

def setup():
    global camera, aruco_dict, parameters
    camera = HizlandirilmisPiKamera()
    camera.veriOkumayaBasla()
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create()
    motors.setSpeeds(0, 0)
    g.setmode(g.BCM)
    g.setup(26, g.IN, pull_up_down=g.PUD_DOWN)
    print(g.input(26))

def forward(n):
    motors.setSpeeds(240, 240) #max: 480
    sleep(n)
    motors.setSpeeds(0, 0)

def back(n):
    motors.setSpeeds(-240, -240)
    sleep(n)
    motors.setSpeeds(0, 0)
    
def takePic():
    global commands, camera, aruco_dict, parameters
    frame = camera.veriOku()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ids = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)[1]

    if ids is None or len(ids) == 0:
        print("no aruco")
        return
    
    ids = ids.tolist()
    commands = []
    for i in ids:
        commands += i
        print(i)
        
    #if ids is not None and len(ids) > 0:print(ids.tolist()) #0, 18, 20, 39

def run():
    global commands
    n = 1
    for i in commands:
        if i == 12:
            back(n)
            n = 1
        if i == 13:
            forward(n)
            n = 1
        if i == 9: n = 3

def takeInput():
    
    while(1):
        y = g.input(26)
        if (y == True):
            print("ey")
            takePic()
            run()
        if (xy != controller.verileriOku()):
           lx, ly = controller.solVerileriOku()
           rightSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx,ly, True)
           leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme(lx,ly, False)
           s.kumandaVerisiniMotorVerilerineCevirme(lx,ly, False)
           motors.hizlariAyarla(rightSpeed, leftSpeed)
 
            
        sleep(0.2)
        
setup()
sleep(1)
thread = threading.Thread(target=takeInput)
thread.start()
while(1):
    frame = camera.veriOku()
    sleep(0.05)
