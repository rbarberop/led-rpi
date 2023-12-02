from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)

while True:
  for i in range (0,32):
    for j in range (0,8):
      pixels[tomatrix(i,j)]=(5,0,0)
      pixels.show()
      sleep(0.02)
      pixels.fill((0,0,0))
  for i in range (0,8):
    for j in range (0,32):
      pixels[tomatrix(j,i)]=(0,5,0)
      pixels.show()
      sleep(0.02)
      pixels.fill((0,0,0))
