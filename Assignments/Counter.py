from adafruit_circuitplayground import cp

import time
import random

cp.pixels.brightness = 0.05

count = 0

cp.pixels.fill((0,0,0))

while True:
    if cp.button_a:
        if count < 10:
            cp.pixels[count] = (255,0,0)
            count += 1
            time.sleep(0.2)

    if cp.button_b:
        if count > 0:
            count -= 1
            cp.pixels[count] = (0, 0, 0)
            time.sleep(0.2)