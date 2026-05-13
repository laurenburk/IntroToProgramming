from adafruit_circuitplayground import cp

import time

cp.pixels.brightness = 0.2

while True:
    temp_c = cp.temperature
    temp_f = (temp_c * 9 / 5) + 32

    if temp_f < 78:
        cp.pixels[0] = (0, 0, 150)

    elif temp_f > 78 and temp_f <= 79:
        cp.pixels[1] = (0, 0, 150)

    elif temp_f > 79 and temp_f <= 80:
        cp.pixels[2] = (0, 0, 150)

    elif temp_f > 80 and temp_f <= 81:
        cp.pixels[3] = (150, 150, 0)

    elif temp_f > 81 and temp_f <= 82:
        cp.pixels[4] = (150,150, 0)

    elif temp_f > 82 and temp_f <= 83:
        cp.pixels[5] = (150,150, 0)

    elif temp_f > 83 and temp_f <= 84:
        cp.pixels[6] = (150, 150, 0)

    elif temp_f > 84 and temp_f <= 85:
        cp.pixels[7] = (150, 0, 0)
    
    elif temp_f > 85 and temp_f <= 86:
        cp.pixels[8] = (150, 0, 0)

    elif temp_f > 86:
        cp.pixels[9] = (150, 0, 0)

    
    time.sleep(.5)