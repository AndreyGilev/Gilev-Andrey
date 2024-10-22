import RPi.GPIO as gpio
import time
import numpy as np
import matplotlib.pyplot as plt

comp = 14
troyka = 13
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT)
gpio.setup(comp, gpio.IN)

def binary(n):
    a = [0] * 8
    for i in range(8):
        a[8-i-1] = n % 2   
        n = n//2
    return a

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2**i 
        gpio.output(dac, binary(k))
        time.sleep(0.01)
        if gpio.input(comp) == 1:
            k-=2**i
    return k



try:
    arr = np.array([])
    k = 0
    count = 0
    t1 = time.time() 
    gpio.output(troyka, 1)

    while k <= 206:
        count += 1
        k = adc()
        arr = np.append(arr, k)
        print(k)
    gpio.output(troyka, 0)

    while k >= 0.02 * 256:
        count += 1
        k = adc()
        arr = np.append(arr, int(k))
        print(k)

    t2 = time.time()
    a = np.array([])

    for i in range(count):
        a = np.append(a, i)
    with open('data.txt', 'w') as data:
        for i in range(count):
            data.write(str(int(arr[i])) + ' ')
    with open('settings.txt', 'w') as set:
        s = 'Частота дискретизации: '+ str(count/(t2-t1)) + "Шаг квантования: " + str(3.3/255)
        set.write(s)
        
    print("Время: ", t2-t1, "Период одного измерения: ", (t2-t1)/count, "Частота дискретизации: ", count/(t2-t1), "Шаг квантования: ", 3.3/255)
    plt.plot(a, arr)
    plt.show()
finally:
    gpio.output(dac, 0)
    gpio.cleanup()