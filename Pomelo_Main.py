import cv2
import cv2.aruco as aruco
from time import sleep
from pololu_drv8835_rpi import motors
import threading
#sudo modprobe bcm2835-v4l2 //this makes picamera visible

commands = [] #Commands array that we will execute

#Setup function to define stuff
def setup():
    global cap, aruco_dict, parameters
    cap = cv2.VideoCapture(-1)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_250)
    parameters = aruco.DetectorParameters_create()
    motors.setSpeeds(0, 0) #Stop motors
    
#Takes a picture with openCV
def takePic():
    global commands, cap, aruco_dict, parameters
    ret, frame = cap.read()
    ret, frame = cap.read() #Read twice to make sure the frame is the most current frame
    
    #If can't take picture, return
    if not ret:
        print("no pic")
        return
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ids = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)[1]

    #If no arucos found, return
    if ids is None or len(ids) == 0:
        print("no aruco")
        return
    
    #Prints the found arucos
    ids = ids.tolist()
    commands = []
    for i in ids:
        commands += i
        print(i)

#Runs the commands (Note: If called more than one times in a row, it will execute the same commands until takePic() is called again.)
def run():
    global commands
    n = 1 #Number of times to execute a function
    for i in commands:
        if i < 10:
            n = i #First 9 blocks sets the n
            
        #More arucos can be added by checking different i values
        if i == 11:
            back(n)
            n = 1
        if i == 12:
            forward(n)
            n = 1

#Takes input from console to take a picture or run the current commands
def takeInput():
    while(1):
        try: n = int(input("1 - take pic\n2 - run\n"))
        except: continue
        if n == 1:
            takePic()
        if n == 2:
            run()

#Put custom functions after this
def forward(n):
    motors.setSpeeds(240, 240) #Max Speed: 480
    sleep(n)
    motors.setSpeeds(0, 0)

def back(n):
    motors.setSpeeds(-240, -240)
    sleep(n)
    motors.setSpeeds(0, 0)
    

setup()
thread = threading.Thread(target=takeInput) #Takes input from console in another thread
thread.start() #Starts the thread
while(1):
    ret, frame = cap.read() #Refresh frames
    sleep(0.05) #Tiny delay
