# This function draws a frame in the color passed as argument

def drawframe(pixels, color):
    from tomatrix import tomatrix
    for i in (0,32):
        pixels[tomatrix(i,0)]=color
        pixels[tomatrix(i,7)]=color
    for j in (0,8):
        pixels[tomatrix(0,j)]=color
        pixels[tomatrix(31,j)]=color
    pixels.show()