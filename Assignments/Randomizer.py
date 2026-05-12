from adafruit_circuitplayground import cp

import time
import random

cp.pixels.brightness = 0.05

while True:
    x, y, z = cp.acceleration
    print("X:", x, "Y:", y, "Z:", z)
    
    shake_threshold = 30.0  # Example threshold value
    if abs(x) > shake_threshold or abs(y) > shake_threshold or abs(z) > shake_threshold:
        for i in range(0,10):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            cp.pixels[i] = (r, g, b)
