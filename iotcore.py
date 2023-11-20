# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel


# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 60

# Prepare the 'Hexagon'. Array with six elements (one per side).
# then each element (side) is an array that contains the LEDs on that side 
side0 = []
side1 = []
side2 = []
side3 = []
side4 = []
side5 = []

for i in range(0,10):
    side0.append(i)
for i in range(10,20):
    side1.append(i)
for i in range(20,30):
    side2.append(i)
for i in range(30,40):
    side3.append(i)
for i in range(40,50):
    side4.append(i)
for i in range(50,60):
    side5.append(i)

hexagon = []
hexagon.append(side0)
hexagon.append(side1)
hexagon.append(side2)
hexagon.append(side3)
hexagon.append(side4)
hexagon.append(side5)

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

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

