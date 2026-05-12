from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.05

while True:
    if cp.switch:
        cp.pixels.fill((0,0,0))
        for i in range(0,5):
                cp.pixels[i] = (0,255,0)
    else:
        cp.pixels.fill((0,0,0))
        for i in range(5,10):
                cp.pixels[i] = (0,255,0)