from time import sleep
import board
import neopixel
pixels = neopixel.NeoPixel(board.D18, 256, auto_write=False)


for i in range (0,256):
  pixels[i]=(0,0,0)  

pixels.show()
