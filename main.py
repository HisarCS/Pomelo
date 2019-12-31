import Main_Lib
from time import sleep
import threading

#GPIO.setmode(GPIO.BCM)

#Aruco = Main_Lib.Aruco()
Monitor = Main_Lib.Monitor()
sleep(1)

#ArucoThread = threading.Thread(target=Aruco.takeInput)
MonitorThread = threading.Thread(target=Monitor.Loop)

#ArucoThread.start()
MonitorThread.start()
print("ThreadStart")

while True:
    """frame = Aruco.camera.veriOku()
    Aruco.camera.kareyiGoster()"""
    pass
