
from PiWarsTurkiyeRobotKiti2019 import HizlandirilmisPiKamera
from time import sleep

camera = HizlandirilmisPiKamera()
camera.veriOkumayaBasla()
sleep(1)
camera.kareyiGoster()
