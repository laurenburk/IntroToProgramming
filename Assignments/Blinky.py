from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.05

while True:
    cp.pixels.fill((0,225,0))
    time.sleep(.367)
    cp.pixels.fill((0,0,0))
    time.sleep(.367)