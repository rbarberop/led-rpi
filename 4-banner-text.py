from time import sleep
import board
import neopixel
from ledutils.tomatrix import tomatrix
from ledutils.drawframe import drawframe
from ledutils.font import letter
from ledutils.smallfont import smallletter
pixels = neopixel.NeoPixel(board.D18, 256, brightness=0.025, auto_write=False)
from random import randint

#letter(pixels, "a",1,(0,255,0))
#letter(pixels, "b",7,(0,0,255))
#letter(pixels, "c",13,(255,0,0))
#letter(pixels, "d",19,(255,255,0))
#letter(pixels, "e",25,(255,0,255))

smallletter(pixels, "a",0,(0,255,0))
smallletter(pixels, "b",5,(0,0,255))
smallletter(pixels, "c",10,(255,0,0))
smallletter(pixels, "d",15,(255,255,0))
smallletter(pixels, "e",20,(255,0,255))
smallletter(pixels, "f",25,(0,255,255))
