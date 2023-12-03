# Draws a pixel only if inside the matrix
# Useful when running banners, where index
# might be out of bounds

from .tomatrix import tomatrix

def drawpixel(pixel, col, row, color):
    minpos = 0
    maxpos = 255

    pos = tomatrix(col, row)

    if minpos <= pos <= maxpos:
        pixel[pos]=color 