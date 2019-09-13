from Side_Lib.MotorKontrol import MotorKontrol
from time import sleep


class Motors():

    def __init__(self):
        self.motors = Side_Lib.MotorKontrol()
        self.motors.hizlariAyarla(0, 0)

    def forward(self, duration):
        self.motors.hizlariAyarla(240, 240)  # max: 480
        sleep(duration)
        self.motors.hizlariAyarla(0, 0)

    def back(self, duration):
        self.motors.hizlariAyarla(-240, -240)
        sleep(duration)
        self.motors.hizlariAyarla(0, 0)

    def right(self, duration):
        self.motors.hizlariAyarla(-240, 240)
        sleep(duration)
        self.motors.hizlariAyarla(0, 0)

    def left(self, duration):
        self.motors.hizlariAyarla(240, -240)
        sleep(duration)
        self.motors.hizlariAyarla(0, 0)

    def AdjustSpeed(self, rightSpeed, leftSpeed):
        self.motors.hizlariAyarla(rightSpeed, leftSpeed)

    def translateControllerDataToMotorData(self, lx, ly):
        self.motors.kumandaVerisiniMotorVerilerineCevirme(lx, ly)