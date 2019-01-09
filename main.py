import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
#sudo modprobe bcm2835-v4l2 //this makes picamera visible

commands = []

def setup():
    global cap, aruco_dict, parameters
    cap = cv2.VideoCapture(-1)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create()
    motors.setSpeeds(0, 0)

def forward(n):
    motors.setSpeeds(240, 240) #max: 480
    sleep(n)
    motors.setSpeeds(0, 0)

def back(n):
    motors.setSpeeds(-240, -240)
    sleep(n)
    motors.setSpeeds(0, 0)
    
def takePic():
    global commands, cap, aruco_dict, parameters
    ret, frame = cap.read()
    ret, frame = cap.read()
    
    if not ret:
        print("no pic")
        return
    
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
    #cv2.imshow('frame',frame)

def run():
    global commands
    n = 1
    for i in commands:
        if i == 6:
            back(n)
            n = 1
        if i == 8:
            forward(n)
            n = 1
        if i == 9: n = 3

def takeInput():
    while(1):
        try: n = int(input("1 - take pic\n2 - run\n"))
        except: continue
        if n == 1:
            takePic()
        if n == 2:
            run()
    

setup()
thread = threading.Thread(target=takeInput)
thread.start()
while(1):
    ret, frame = cap.read()
    sleep(0.05)
