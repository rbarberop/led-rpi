from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
from ledutils.drawframe import drawframe
pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.025, auto_write=False)
from random import randint

framecolor = (255,255,255)

while True:
  drawframe(pixels,framecolor)
  sleep(2)
  fillcolor = (randint(0,255),randint(0,255),randint(0,255))
  for i in range (1,31):
    for j in range (1,7):
      pixels[tomatrix(i,j)]=fillcolor
      pixels.show()
      sleep(0.02)
  drawframe(pixels,framecolor)
  sleep(2)
  fillcolor = (randint(0,255),randint(0,255),randint(0,255))
  for i in range (1,7):
    for j in range (1,31):
      pixels[tomatrix(j,i)]=fillcolor
      pixels.show()
      sleep(0.02)

