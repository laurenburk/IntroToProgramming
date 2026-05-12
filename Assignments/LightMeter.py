from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.05

cp.pixels.fill((0,0,0))

while True:
    light_level = cp.light

    num_pixels = int(1 + (30 - light_level) / 3)

    if num_pixels < 0:
        num_pixels = 0
    if num_pixels > 10:
        num_pixels = 10

    for i in range(10):
        if i < num_pixels:
            cp.pixels[i] = (0, 0, 255)
        else:
            cp.pixels[i] = (0, 0, 0)
    
    time.sleep(0.1)