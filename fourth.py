import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
gpio_out = 24
gpio.setup(gpio_out, gpio.OUT)
a = [2, 3, 4, 17, 27, 22, 10, 9]
gpio.setup(a, gpio.OUT)
gpio.output(a, 0)

p = gpio.PWM(gpio_out, 10000)
n = 0
try:
    
    while True:
        p.start(n)
        n = int(input())
        
finally:
    p.stop()
    gpio.output(gpio_out, 0)

