from pololu_drv8835_rpi import motors
import math



class MotorKontrol:

    def __init__(self):
        self.hizSag = 0
        self.hizSol = 0

    def hizlariAyarla(self, hizSag, hizSol):

        self.hizSag = hizSag
        self.hizSol = hizSol

        480 if hizSag>480 else hizSag
        -480 if hizSag < -480 else hizSag

        480 if hizSol > 480 else hizSol
        -480 if hizSol < -480 else hizSol


        motors.setSpeeds(hizSag, hizSol)

    def kumandaVerisiniMotorVerilerineCevirme(self, x, y):
        
        r = math.hypot(x, y)
        t = math.atan2(y, x)

        # rotate by 45 degrees
        t += math.pi / 4

        # back to cartesian
        left = r * math.cos(t)
        right = r * math.sin(t)

        # rescale the new coords
        left = left * math.sqrt(2)
        right = right * math.sqrt(2)
 
        # clamp to -1/+1
        left = max(-1, min(left, 1))
        right = max(-1, min(right, 1))

        return int(left * 480), -int(right * 480)
