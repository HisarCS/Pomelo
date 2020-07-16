import Main_Lib
from time import sleep
import threading
import queue

GPIO.setmode(GPIO.BCM)

lock = threading.Lock()
queue = queue.Queue()
queue2 = queue.Queue()
queue3 = queue.Queue()

Aruco = Main_Lib.Aruco()
Monitor = Main_Lib.Monitor()
SiteFlask = Main_Lib.PomeloFlask()
sleep(1)

ArucoThread = threading.Thread(target=Aruco.takeInput, args=(lock, queue, queue2, queue3))
MonitorThread = threading.Thread(target=Monitor.Loop, args=(queue))
FlaskThread = threading.Thread(target=SiteFlask.Loop, args=(queue2, queue3))

ArucoThread.start()
MonitorThread.start()
FlaskThread.start()
print("ThreadStart")

while True:
    frame = Aruco.camera.veriOku()
    Aruco.camera.kareyiGoster()
    pass