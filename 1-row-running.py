from time import sleep
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)

while True:
  for i in range (0,31):
    for j in range (1,8):
      pixels[i*j]=(5,0,0)
      pixels.show()
      sleep(0.2)
      pixels[i*j]=(0,0,0)

