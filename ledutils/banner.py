# Banner

from .tomatrix import tomatrix
from .smallfont import smallletter
from time import sleep


def banner(pixel, line, color):
  for a in range (0,32):
    smallletter(pixel, line[0], a, (0,255,0))
    sleep(0.2)
    pixel.fill(0,0,0)

