import pygame
import sys
import random
screen = pygame.display.set_mode((480,272), )
pygame.init()
pygame.display.set_caption("Pomelo")

black=(0,0,0)
white=(255,255,255)
screen.fill(white)

while True:
  #6741abc. photon sifre
  pygame.display.update()
  myfont = pygame.font.SysFont("monospace", 170)
  #label = myfont.render("Hisar CS Pinball", 1, white)
  #screen.blit(label, (5, 200))
  for event in pygame.event.get():
      if event.type == pygame.QUIT:
          pygame.quit()
          sys.exit()
      if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_q:
              pygame.display.toggle_fullscreen()
