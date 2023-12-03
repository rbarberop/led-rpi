from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
from ledutils.drawframe import drawframe
from ledutils.font import letter
from ledutils.smallfont import smallletter
from ledutils.banner import banner
pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.025, auto_write=False)
from random import randint


banner(pixels, "a", (0,255,0))

