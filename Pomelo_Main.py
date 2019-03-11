import cv2.aruco as aruco
import cv2
import sys
import pygame
import threading
from PiWarsTurkiyeRobotKiti2019 import MotorKontrol
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
import RPi.GPIO as GPIO
from time import sleep

# sudo modprobe bcm2835-v4l2 //this makes picamera visible


motors = MotorKontrol ()
# controller = PiWarsTurkiyeRobotKiti2019.Kumanda ()
# controller.dinlemeyeBasla ()
# xy = controller.solVerileriOku ()
# xz = controller.sagVerileriOku ()
# xx = controller.butonlariOku ()
commands = []

white = (255, 255, 255)
screen = pygame.display.set_mode ((480, 272), )
pygame.init ()
pygame.display.set_caption ("Pomelo")
Emotions = []
Neutral_Happy2 = []
Blink = []
Road_to_sleep = []
#I_am_sleeping = []
Emotions.append (Blink)
Emotions.append (Neutral_Happy2)
#Emotions.append(Road_to_sleep)
#Emotions.append(I_am_sleeping)
emotion_number = 0
elma = 0
ongoing_emotion = 0


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


def Happys():
    for x in range (37):
        Neutral_Happy2.append (pygame.transform.scale (
            pygame.image.load ('./Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.' + str (x) + '.jpeg'),
            (480, 272)))

def To_Sleep():
    for x in range (18):
        Road_to_sleep.append (pygame.transform.scale (
            pygame.image.load ('./Pomelo_Face/To_Sleep/Pomelo_Eyes_GoToSleep.' + str (x) + '.jpeg'),
            (480, 272)))
"""        
def Sleeping():
    for x in range (37):
        I_am_sleeping.append (pygame.transform.scale (
            pygame.image.load ('./Pomelo_Face/To_Sleep/Pomelo_Eyes_Sleep.' + str (x) + '.jpeg'),
            (480, 272)))
"""
def Blinks():
    for x in range (37):
        Blink.append (
            pygame.transform.scale (pygame.image.load ('./Pomelo_Face/Blink/Pomelo_Eyes_Blink.' + str (x) + '.jpeg'),
                                    (480, 272)))


def check_emotion(ongoing_emotion, emotion_number, emotion_count):
    if ongoing_emotion == 1:
        Blit_Face (emotion_number, emotion_count)
        emotion_count += 1
    if ongoing_emotion == 0:
        No_Emotion ()
    return emotion_count


def No_Emotion():
    screen.blit (Emotions[0][0], (0, 0))


def Blit_Face(emotion_number, emotion_count):
    screen.blit (Emotions[emotion_number][emotion_count], (0, 0))

    Pause (0.00001)


# fill screen white
def Clear_Screen():
    screen.fill (white)


def Update_Screen():
    pygame.display.update ()


# enter fullscreen
def Enter_FullScreen():
    screen = pygame.display.set_mode ((480, 272), pygame.FULLSCREEN)


def Exit_FullScreen():
    screen = pygame.display.set_mode ((480, 272), )


def Exit_Screen():
    pygame.quit ()
    sys.exit ()


def Pause(duration2):
    sleep (duration2)


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
    if len (commands) >= 1:
        print(len (commands))
        for i in range (len (commands)):
            print(i)
            arucoNumber = commands[i]
            if len (commands) - 1 > i:
                arucoNumberSecond = commands[i + 1]
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
        thread
        if (y == True):
            print("button pressed")
            takePic ()
            run ()
        """while (xx != controller.butonlariOku () or xy != controller.sagVerileriOku () or xz != controller.solVerileriOku ()):
            lx, ly = controller.solVerileriOku ()
            print(lx, ly)
            rightSpeed, leftSpeed = motors.kumandaVerisiniMotorVerilerineCevirme (lx, ly)
            print(lx, " ", ly, " ", rightSpeed, " ", leftSpeed)
            motors.hizlariAyarla (rightSpeed, leftSpeed)
            sleep (0.3)
            motors.hizlariAyarla (0, 0)"""

        sleep (0.2)


def Monitor_loop(elma, ongoing_emotion):
    while (1):
        Clear_Screen ()
        elma = check_emotion (ongoing_emotion, emotion_number, elma)
        if elma == 36:
            elma = 0
            ongoing_emotion = 0
        else:
            ongoing_emotion = 0
        Update_Screen ()
        for event in pygame.event.get ():
            if event.type == pygame.QUIT:
                Exit_Screen ()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:  # if e key is pressed
                    Enter_FullScreen ()
                if event.key == pygame.K_x:  # if x key is pressed
                    Exit_FullScreen ()
                if event.key == pygame.K_q:  # if q key is pressed
                    Exit_Screen ()


setup ()
Happys ()
Blinks ()
To_Sleep()
#Sleeping()
sleep (1)
"""
thread1 = threading.Thread (target=takeInput ())
thread2 = threading.Thread (target=Monitor_loop (elma, ongoing_emotion))
thread2.start ()
thread1.start ()

while (1):
    frame = camera.veriOku ()
    # camera.kareyiGoster()
"""
thread1 = threading.Thread (target=takeInput)
thread2 = threading.Thread (target=camera.veriOku())
thread1.start ()
thread2.start ()

Monitor_loop(elma, ongoing_emotion)
