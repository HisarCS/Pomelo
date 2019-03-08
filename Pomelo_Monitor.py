import pygame
import sys
from time import sleep

class Monitor:

    def __init__(self):
        self.white=(255,255,255)
        self.screen = pygame.display.set_mode ((480, 272), )
        #monitor setup
        pygame.init ()
        pygame.display.set_caption("Pomelo")
        #emotion setup
        self.Emotions = []
        self.Neutral_Happy2 =[]
        self.Blink = []
        self.Emotions.append(self.Neutral_Happy2)
        self.Emotions.append(self.Blink)
        self.emotion_number = 1
        self.emotion_count = 0
        self.ongoing_emotion = 1
        self.Blinks()
        self.Happys ()
        

    def Happys(self):
        for x in range (37):
            self.Neutral_Happy2.append(pygame.transform.scale(pygame.image.load('./Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.'+str(x)+'.jpeg') , (480,272)))

    def Blinks(self):
        for x in range (37):
            self.Blink.append(pygame.transform.scale(pygame.image.load('./Pomelo_Face/Blink/Pomelo_Eyes_Blink.'+str(x)+'.jpeg'), (480, 272)))

    #setup finished

    #check if an emotion is displayed
    def check_emotion(self, ongoing_emotion, emotion_number, emotion_count):
        if ongoing_emotion == 1:
            self.Blit_Face(emotion_number, emotion_count)
            self.emotion_count += 1
        if ongoing_emotion == 0:
            self.No_Emotion()

    # when no emotion is displayed
    def No_Emotion(self):
        self.screen.blit (self.Emotions[0][0], (0, 0))

    # display emotion
    def Blit_Face(self, emotion_number, emotion_count):
        self.screen.blit (self.Emotions[emotion_number][emotion_count], (0, 0))
        self.Pause(0.00001)
        if self.emotion_count == 36:
            self.emotion_count = -1
            self.ongoing_emotion = 1
        else:
            self.ongoing_emotion = 1

    #fill screen white
    def Clear_Screen(self):
        self.screen.fill (self.white)

    def Update_Screen(self):
        pygame.display.update ()

    #enter fullscreen
    def Enter_FullScreen(self):
        self.screen = pygame.display.set_mode ((480, 272), pygame.FULLSCREEN)

    #enter fullscreen
    def Exit_FullScreen(self):
        self.screen = pygame.display.set_mode ((480, 272), )

    #end pygame
    def Exit_Screen(self):
        pygame.quit ()
        sys.exit ()

    #code pauses of amount of seconds given
    def Pause(self, duration):
        sleep (duration)


LCD = Monitor()

while True:
    LCD.Clear_Screen()
    #camera must detect emotion
    # search emotion in list
    #emotion_number is = to emotions number in Emotions list
    #LCD.ongoing_emotion = 1
    LCD.check_emotion(LCD.ongoing_emotion, LCD.emotion_number, LCD.emotion_count)
    LCD.Update_Screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            LCD.Exit_Screen()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e: #if e key is pressed
                LCD.Enter_FullScreen()
            if event.key == pygame.K_x: #if x key is pressed
                LCD.Exit_FullScreen()
            if event.key == pygame.K_q: #if q key is pressed
                LCD.Exit_Screen()
