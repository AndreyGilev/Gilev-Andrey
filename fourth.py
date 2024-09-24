import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
gpio.setup(dac, gpio.OUT)

def tran(n):
    n2 = [0] * 8
    for i in range(8):
        n2[i] = n%2
        n//=2
    return n2
period = float(input())

try:
    while True:
        for n in range(256):
            n2 = tran(n)
            gpio.output(dac, n2)
            time.sleep(period/512)
        for n in range(255, -1, -1):
            n2 = tran(n)
            gpio.output(dac, n2)
            time.sleep(period/512)
finally:
    gpio.output(dac, 0)