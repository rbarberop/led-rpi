from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
from ledutils.drawframe import drawframe
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)

color = (5,5,5)

while True:
  drawframe(pixels,color)
  sleep(2)
  for i in range (0,32):
    for j in range (0,8):
      pixels[tomatrix(i,j)]=(5,0,0)
      pixels.show()
      sleep(0.02)
      pixels[tomatrix(i,j)]=(0,0,0)
  drawframe(pixels,color)
  sleep(2)
  for i in range (0,8):
    for j in range (0,32):
      pixels[tomatrix(j,i)]=(0,5,0)
      pixels.show()
      sleep(0.02)
      pixels[tomatrix(j,i)]=(0,0,0)

