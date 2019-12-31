import Main_Lib
from time import sleep
import threading
import queue

GPIO.setmode(GPIO.BCM)

lock = threading.Lock()
queue = queue.Queue()

Aruco = Main_Lib.Aruco()
Monitor = Main_Lib.Monitor()
sleep(1)

ArucoThread = threading.Thread(target=Aruco.takeInput, args=(lock, queue))
MonitorThread = threading.Thread(target=Monitor.Loop, args=(lock))

ArucoThread.start()
MonitorThread.start()
print("ThreadStart")

while True:
    frame = Aruco.camera.veriOku()
    Aruco.camera.kareyiGoster()
    pass
