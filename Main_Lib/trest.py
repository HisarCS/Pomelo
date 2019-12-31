import pygame

white = (255, 255, 255)
screen = pygame.display.set_mode((480, 272), )

# monitor setup
pygame.init()
pygame.display.set_caption("Pomelo")

Neutral_Happy2 = []
Blink = []
Angry = []

ongoing = 0


def Happys():
    global Neutral_Happy2
    for x in range(37):
        Neutral_Happy2.append(pygame.transform.scale(pygame.image.load(
            '/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.' + str(x) + '.jpeg'), (480, 272)))


def Blinks():
    global Blink
    for x in range(37):
        Blink.append(pygame.transform.scale(
            pygame.image.load('/home/pi/pomelo/Pomelo_Face/Blink/Pomelo_Eyes_Blink.' + str(x) + '.jpeg'), (480, 272)))

        '''def AngryBlit():
            global Angry
            global ongoing
            ongoing = 1
            for x in range(37):
                screen.blit(Angry[x], (0,0))
            ongoing = 0
        def Angrys():
            global Angry
            for x in range (37):
                Angry.append(pygame.transform.scale(pygame.image.load(/home/pi/pomelo/Pomelo_Face/Angry/Pomelo_Eyes_Neutral_Angry.+str(x)+.jpeg), (480,272)))        
        '''


def HappyBlit():
    global Neutral_Happy2
    global ongoing
    ongoing = 1
    for x in range(37):
        screen.blit(Neutral_Happy2[x], (0, 0))
    ongoing = 0


def BlinkBlit():
    global Blink
    global ongoing
    ongoing = 1
    for x in range(37):
        screen.blit(Blink[x], (0, 0))
    ongoing = 0


while True:
    if ongoing == 0:
        screen.blit(pygame.transform.scale(
            pygame.image.load('/home/pi/pomelo/Pomelo_Face/Neutral-Happy2/Pomelo_Eyes_Neutral-Happy2.' + '0' + '.jpeg'),
            (480, 272)), (0, 0))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:  # if e key is pressed
                # self.Happys()
                print("Hap")
            if event.key == pygame.K_a:  # if x key is pressed
                # self.Angrys()
                print("Ang")
