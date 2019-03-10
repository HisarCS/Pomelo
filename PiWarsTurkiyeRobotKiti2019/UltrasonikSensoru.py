from time import sleep, time
import RPi.GPIO as GPIO
from threading import Thread
import PiWarsTurkiyeRobotKiti2019

class UltrasonikSensoru:

    def __init__(self, echo, trig, setup=GPIO.BOARD):

        self.echo = echo
        self.trig = trig

        self.sure = 0

        self.mesafe = list()
        self.anlikOlcum = 0

        GPIO.setmode(setup)

        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

        GPIO.output(trig, False)

    def mesafeOlcmeyeBasla(self):

        Thread(target=self.__mesafeOlc__, args=()).start()
        sleep(0.2)

    def mesafeOku(self):
        return self.mesafe[8], self.anlikOlcum

    def __mesafeOlc__(self):

        while True:
            GPIO.output(self.trig, True)
            sleep(0.0001)
            GPIO.output(self.trig, False)

            sinyal_baslangic = time()
            saglikliOlcum = 1

            while GPIO.input(self.echo) == 0:
                if abs(sinyal_baslangic - time()) > 0.03:
                    saglikliOlcum = 0
                    break

            # save time of arrival
            while GPIO.input(self.echo) == 1 and saglikliOlcum:
                sinyal_bitis = time()

            if saglikliOlcum:
                self.sure = sinyal_bitis - sinyal_baslangic
                self.anlikOlcum = self.sure * 17150
                self.mesafe.append(self.anlikOlcum)
                self.mesafe.sort()
                if len(self.mesafe) > 16:
                    self.mesafe.pop()
                    self.mesafe.pop(0)

