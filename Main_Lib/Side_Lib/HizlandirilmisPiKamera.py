
from picamera import PiCamera
from picamera.array import PiRGBArray
from threading import Thread
import imutils
import cv2
from time import sleep

class HizlandirilmisPiKamera:

    def __init__(self, cozunurluk=(640, 480)):

        self.camera = PiCamera()
        self.camera.resolution = cozunurluk
        self.hamKare = PiRGBArray(self.camera, size=self.camera.resolution)
        self.yayin = self.camera.capture_continuous(self.hamKare, format="bgr", use_video_port=True)
        self.suAnkiKare = None

        self.penceredeGosterilecekler = dict()
        self.kameraGostermeAktif = False

    def veriOkumayaBasla(self):

        Thread(target=self.__veriGuncelle__, args=()).start()
        return self

    def __veriGuncelle__(self):

        for f in self.yayin:

            self.suAnkiKare = f.array
            self.hamKare.truncate(0)

    def veriOku(self):

        return self.suAnkiKare

    def kareyiGoster(self, pencereninIsmi="frame", gosterilecekGoruntu=None):
        if gosterilecekGoruntu is None:
            self.penceredeGosterilecekler[pencereninIsmi] = self.suAnkiKare
        else:
            self.penceredeGosterilecekler[pencereninIsmi] = gosterilecekGoruntu

        if not self.kameraGostermeAktif:
            Thread(target=self.__kareyiGostermeyiGuncelle__, args=()).start()

    def __kareyiGostermeyiGuncelle__(self):

        self.kameraGostermeAktif = True

        while True:

            for isim in self.penceredeGosterilecekler.copy():
                cv2.imshow(isim, self.penceredeGosterilecekler[isim])

            key = cv2.waitKey(1)

            if key == ord("q"):
                cv2.destroyAllWindows()
                break
