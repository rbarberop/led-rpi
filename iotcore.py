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
hexagon = []
for i in range(1,10):
    hexagon[0].append(i)
for i in range(11,20):
    hexagon[1].append(i)
for i in range(21,30):
    hexagon[2].append(i)
for i in range(31,40):
    hexagon[3].append(i)
for i in range(41,50):
    hexagon[4].append(i)
for i in range(51,60):
    hexagon[5].append(i)

# The order of the pixel colors - RGB or GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)

def initial_color():
    # Blue and white alternating
    for p in hexagon[0]:
        pixel[p]=(255,255,255)
    for p in hexagon[1]:
        pixel[p]=(0,0,255)
    for p in hexagon[2]:
        pixel[p]=(255,255,255)
    for p in hexagon[3]:
        pixel[p]=(0,0,255)
    for p in hexagon[4]:
        pixel[p]=(255,255,255)
    for p in hexagon[5]:
        pixel[p]=(0,0,255)
        
    
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


while True:
    # rainbow_cycle(0.0001)  # rainbow cycle with .1ms delay per step
    initial_color()
