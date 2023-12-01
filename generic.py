
# Neopixel controller for RPi
#
# This program reads the LED programming from ./config.csv file
#
# The first line of the CSV file has the following structure:
# pixels, brightness, o/t/j, delay
# 
# Where: 
#   * pixels - number of pixels to control
#   * brightness - number between 0.1 and 1
#   * o - oneway - LED color goes from start to end by increment, then jumps to start color and repeats
#   * t - twoway - LED color goes from start to end by increment, then decreases increment to start and repeats (cycles)
#   * j - jump   - LED color goes from start to end directly, increment is ignored
#   * delay - number of seconds between steps
#
# The rest of the lines configure each of the LEDs on the strip:
# pixel, (s,s,s), (i,i,i), (e,e,e)
#
# Where:
#   * pixel - is the pixel number, starting at 0, can be an interval n-m (means led n to led m)
#   * (s,s,s) - RGB start color
#   * (i,i,i) - increment for each color per step (can be negative)
#   * (e,e,e) - RGB end color
#

import csv
import time
import board
import neopixel

# Class led to store information about each
class led:
    def __init__(start_color, end_color, step):
        self.start_color = start_color
        self.current_color = start_color
        self.end_color = end_color
        self.step = step

    def next():
        if self.current_color < self.end_color:
            self.current_color = self.current_color + self.step

    def previous():
        if self.current_color > self.start_color:
            self.current_color = self.current_color - self.step


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18
ORDER = neopixel.GRB

# Read configuration
with open('./config.csv', 'r') as input_file:
    reader = csv.reader(input_file, delimiter=',')

# Extract general configuration from first line
header = next(reader, None)

# The number of NeoPixels
num_pixels = header[0]
brightness = header[1]
run_mode = header[2]
slee_delay = header[3]

# Prepare pixels matrix

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness, auto_write=False, pixel_order=ORDER
)

# Read pixel control configuration



def initial_color():
    # Blue and white alternating
    for p in hexagon[0]:
        pixels[p]=(255,255,255)
    for p in hexagon[1]:
        pixels[p]=(0,0,255)
    for p in hexagon[2]:
        pixels[p]=(255,255,255)
    for p in hexagon[3]:
        pixels[p]=(0,0,255)
    for p in hexagon[4]:
        pixels[p]=(255,255,255)
    for p in hexagon[5]:
        pixels[p]=(0,0,255)

def blue_white():
    for c in range(0,255,10):
        x = 255 - c
        for p in hexagon[0]:
            pixels[p]=(x,x,255)
        for p in hexagon[1]:
            pixels[p]=(c,c,255)
        for p in hexagon[2]:
            pixels[p]=(x,x,255)
        for p in hexagon[3]:
            pixels[p]=(c,c,255)
        for p in hexagon[4]:
            pixels[p]=(x,x,255)
        for p in hexagon[5]:
            pixels[p]=(c,c,255)
        pixels.show()
        time.sleep(0.1)
    for c in range(255,0,-10):
        x = 255 - c
        for p in hexagon[0]:
            pixels[p]=(x,x,255)
        for p in hexagon[1]:
            pixels[p]=(c,c,255)
        for p in hexagon[2]:
            pixels[p]=(x,x,255)
        for p in hexagon[3]:
            pixels[p]=(c,c,255)
        for p in hexagon[4]:
            pixels[p]=(x,x,255)
        for p in hexagon[5]:
            pixels[p]=(c,c,255)
        pixels.show()
        time.sleep(0.1)
        
    
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        r = g = b = 0
    elif pos < 85:
        r = int(pos * 3)
        g = int(255 - pos * 3)
        b = 0
    elif pos < 170:
        pos -= 85
        r = int(255 - pos * 3)
        g = 0
        b = int(pos * 3)
    else:
        pos -= 170
        r = 0
        g = int(pos * 3)
        b = int(255 - pos * 3)
    return (r, g, b) if ORDER in (neopixel.RGB, neopixel.GRB) else (r, g, b, 0)


def rainbow_cycle(wait):
    for j in range(255):
        for i in range(num_pixels):
            pixel_index = (i * 256 // num_pixels) + j
            pixels[i] = wheel(pixel_index & 255)
        pixels.show()
        time.sleep(wait)

# Main program

initial_color()
pixels.show()
while True:
    blue_white()

