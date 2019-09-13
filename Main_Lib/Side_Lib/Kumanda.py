import pygame
from threading import Thread


class Kumanda:
    
    def __init__(self):
        
        pygame.init()
        
        pygame.joystick.init()
                
        self.j = pygame.joystick.Joystick(0)
        self.j.init()
        
        self.butonlar = []
        self.solX = 0
        self.solY = 0
        self.sagX = 0
        self.sagY = 0

    def dinlemeyeBasla(self):
        
        Thread(target=self.__yenile__, args=()).start()
        return self
    
    def __yenile__(self):
        
        while True:
            for e in pygame.event.get():
                if (e.type == pygame.JOYBUTTONDOWN and e.button not in self.butonlar):
                    self.butonlar.append(e.button)
                if (e.type == pygame.JOYBUTTONUP and e.button in self.butonlar):
                    self.butonlar.remove(e.button)
                if (e.type == pygame.JOYAXISMOTION):
                    if (e.axis == 0):
                        self.solX = e.value
                    elif (e.axis == 1):
                        self.solY = e.value
                    elif (e.axis == 2):
                        self.sagX = e.value
                    elif (e.axis == 3):
                        self.sagY = e.value

    def solVerileriOku(self):
        return self.solX, self.solY
    
    def sagVerileriOku(self):
        return self.sagX, self.sagY
    
    def butonlariOku(self):
        return self.butonlar
    
    def verileriOku(self):
        return self.solVerileriOku(), self.sagVerileriOku(), self.butonlariOku()

