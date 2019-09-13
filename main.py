import Main_Lib
from time import sleep
import threading

GPIO.setmode(GPIO.BCM)

Aruco = Aruco()
Monitor = Monitor()
sleep(1)

ArucoThread = threading.Thread(target=Aruco.takeInput)
MonitorThread = threading.Thread(target=Monitor.Loop)

ArucoThread.start()
MonitorThread.start()

while (1):
    frame = Arucuk.camera.veriOku()
    Arucuk.camera.kareyiGoster()
