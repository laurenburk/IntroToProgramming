from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.05

while True:
    x,y,z = cp.acceleration


    if x > 2:
        for i in range(1,4):
            cp.pixels[i] = (0,255,0)

    elif x < -2:
        for i in range(6,9):
            cp.pixels[i] = (255,0,0)

    else:
        cp.pixels.fill((0,0,0))