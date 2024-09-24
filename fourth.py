import RPi.GPIO as gpio
gpio.setmode(gpio.BCM)
dac = [6, 12, 5, 0, 1, 7, 11, 8]
gpio.setup(dac, gpio.OUT)

def tran(n):
    n2 = [0] * 8
    for i in range(8):
        n2[i] = n%2
        n//=2
    return n2


try:
    while True:
        n = int(input())
        if(n>=0):
            n2 = tran(n)
            gpio.output(dac, n2)
            print(3.3/255 * n)
        else:
            n2 = tran('q')
            gpio.output(dac, n2)
            print(3.3/255 * n)
except Exception:
    print("Ошибка или конец программы")
finally:
    gpio.output(dac, 0)