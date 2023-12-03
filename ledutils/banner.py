# Banner

from .tomatrix import tomatrix
from .smallfont import smallletter
from time import sleep


def banner(pixel, line, color):
  for col in range (32,(-5*(len(line)+1))-1,-1):
    letterpos = 1
    for letter in line:
      smallletter(pixel, letter, col+(5*letterpos)+1, (0,255,0))
      letterpos = letterpos + 1
    sleep(0.1)
    pixel.fill((0,0,0))

