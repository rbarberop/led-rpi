from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
from ledutils.drawframe import drawframe
from ledutils.font import letter
pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.025, auto_write=False)
from random import randint

framecolor = (255,255,255)

drawframe(pixels,framecolor)
sleep(2)

letter(a,3,(0,5,0))

