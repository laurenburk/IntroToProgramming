from adafruit_circuitplayground import cp

import time
import random

cp.pixels.brightness = 0.05

while True:
    if cp.button_a:
        p = random.randint(1, 10)
        cp.pixels.fill((0,0,0))
        for i in range(0,p):
            cp.pixels[i] = (255,0,0)
        time.sleep(.5)    

    if cp.button_b:
        cp.pixels.fill((0,0,0))
        time.sleep(.5)