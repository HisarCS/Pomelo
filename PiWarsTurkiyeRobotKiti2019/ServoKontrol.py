from time import sleep, time
import RPi.GPIO as GPIO
from threading import Thread

class ServoKontrol:
    
    def __init__(self, pin=35, GPIOSetup = GPIO.BOARD):
        GPIO.setmode(GPIOSetup)
        
        GPIO.setup(pin, GPIO.OUT)
        self.pwm = GPIO.PWM(pin, 50)
        self.pwm.start(0)
        self.pin = pin
        self.hedefAci = 90
        self.suankiAci = 90
        self.uyuduMu = True
        self.surekliMi = False

    
    def surekliDonmeyeAyarla(self):
        self.surekliMi = True
        GPIO.output(self.pin, True)
    
    def tekAciDonmeyeAyarla(self):
        self.surekliMi = False
        GPIO.output(self.pin, False)
    
    def __tekAciAyarlaAsil__(self):
        sinyalUzunlugu = self.hedefAci / 18 + 2
        GPIO.output(self.pin, True)
        self.pwm.ChangeDutyCycle(sinyalUzunlugu)

        deltaAci = abs(self.hedefAci - self.suankiAci)
        gerekenUyku = deltaAci / 150
        sleep(gerekenUyku)  # experimental value
        GPIO.output(self.pin, False)
        self.pwm.ChangeDutyCycle(0)
        self.suankiAci = self.hedefAci
        self.uyuduMu = True
    
    def __surekliAciAyarlaAsil__(self, aci):
        duty = aci / 18 + 2
        self.pwm.ChangeDutyCycle(duty)
    
    def aciAyarla(self, aci):

        self.hedefAci = aci

        if self.surekliMi:
            self.__surekliAciAyarlaAsil__(self.hedefAci)
        elif self.uyuduMu and (self.suankiAci is not self.hedefAci):
            self.uyuduMu = False
            
            Thread(target=self.__tekAciAyarlaAsil__(), args=()).start()
