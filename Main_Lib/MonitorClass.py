import pygame
import RPi.GPIO as GPIO
from time import sleep
from ArucoClass import Aruco
import threading
import value

#c = threading.Condition()
#detectedMarkers = None
class Monitor(Aruco):
    def __init__(self):
        self.white=(255,255,255)
        self.screen = pygame.display.set_mode ((480, 272), )

                #monitor setup
        pygame.init ()
        pygame.display.set_caption("Pomelo")

        self.Neutral_Happy2 =[]
        self.Blink = []
        self.Angry = []

        self.ongoing = 0

        self.Happys()
        self.Angrys()
        self.Blinks()
        

    def Happys(self):
        for x in range (37):
            self.Neutral_Happy2.append(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.'+str(x)+'.jpeg') , (480,272)))
            
    def Blinks(self):
        for x in range (37):
            self.Blink.append(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Blink/Pomelo_Eyes_Blink.'+str(x)+'.jpeg'), (480, 272)))


    def Angrys(self):
        for x in range (37):
            self.Angry.append(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Angry/Pomelo_Eyes_Neutral_Angry.'+str(x)+'.jpeg'), (480,272)))

    def AngryBlit(self):
        self.ongoing = 1
        for x in range(37):
            self.screen.blit(self.Angry[x], (0,0))
            pygame.display.update()
        self.ongoing = 0
        sleep(0.2)

                         
    def HappyBlit(self):
        self.ongoing = 1
        for x in range(37):
            self.screen.blit(self.Neutral_Happy2[x], (0,0))
            pygame.display.update()
        self.ongoing = 0
        sleep(0.2)
                         
    def BlinkBlit(self):
        self.ongoing = 1
        for x in range(37):
            self.screen.blit(self.Blink[x], (0,0))
            pygame.display.update()
            sleep(0.2)
        self.ongoing = 0


    def Loop(self, q):    
        while True:
            print('1')
            #if ongoing == 0:
            self.screen.blit(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.'+'0'+'.jpeg'), (480,272)), (0,0))
            
            val = q.get()
            
            if val == 0:
                self.AngryBlit()
                self.screen.blit(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.'+'0'+'.jpeg'), (480,272)), (0,0))
                print("not found")
                pygame.display.update()
            elif val == 1:
                self.HappyBlit()
                self.screen.blit(pygame.transform.scale(pygame.image.load('/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.'+'0'+'.jpeg'), (480,272)), (0,0))
                pygame.display.update()
            
            pygame.display.update()
            
            #self.aruco = super(Monitor,self).takeMonitorInput()

            #self.BlinkBlit()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h: #if e key is pressed
                        self.HappyBlit()
                        print("Hap")
                    if event.key == pygame.K_a: #if x key is pressed
                        self.AngryBlit()
                        print("Ang")
