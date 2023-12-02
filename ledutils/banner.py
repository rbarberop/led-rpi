# Banner

from .tomatrix import tomatrix
from .smallfont import smallfont
from time import sleep


def banner(pixel, line, color):
  for a in range (0,32):
    for i in range(0,5):
      for j in range(0,4):
        for character in line:
          if alphabet[character][i][j] == 0 :
              pixel[tomatrix(j+a,i+2)]=(0,0,0)
          else:
              pixel[tomatrix(j+a,i+2)]=color
    pixel.show()
    sleep(0.2)
    pixel.clear()

