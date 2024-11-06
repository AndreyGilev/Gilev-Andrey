import RPi.GPIO as gpio
import time
import numpy as np
import matplotlib.pyplot as plt

comp = 14
troyka = 13
gpio.setmode(gpio.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT)                    # Настраиваем Gpio
gpio.setup(comp, gpio.IN)


def binary(n):
    a = [0] * 8
    for i in range(8):                          # Функция перевода числа в двоичную запись
        a[8 - i - 1] = n % 2
        n = n // 2
    return a


def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        gpio.output(dac, binary(k))             # Функция, выдающая цифровое значение подаваемого аналогого напряжения
        time.sleep(0.01)
        if gpio.input(comp) == 1:
            k -= 2 ** i
    return k


try:
    arrdigitalU = np.array([])                  # Объявление массива, хранящего значения напржения в цифровом виде
    u = 0
    count = 0
    t1 = time.time()
    gpio.output(troyka, 1)

    while u <= 206:                             # Запонение массива с напряжением при зарядке конденчатора
        count += 1                              # Считаем, сколько отсчетов приходит
        u = adc()
        arrdigitalU = np.append(arrdigitalU, u)
        print(u)
    gpio.output(troyka, 0)

    while u >= 0.02 * 256:                      # Запонение массива с напряжением при разрядке конденчатора
        count += 1
        u = adc()
        arrdigitalU = np.append(arrdigitalU, int(u))
        print(u)

    t2 = time.time()
    counter = np.array([])

    for i in range(count):                      # Заполнение массива числа отсчетов
        counter = np.append(counter, i)
    with open('data.txt', 'w') as data:         # Запись в текстовый файл цифровых значений напряжения
        for i in range(count):
            data.write(str(int(arrdigitalU[i])) + ' ')
    with open('settings.txt', 'w') as set:      # Запись в другой текстовый файл параметров системы
        s = 'Частота дискретизации: ' + str(count / (t2 - t1)) + "Шаг квантования: " + str(3.3 / 255)
        set.write(s)

    print("Время: ", t2 - t1, "Период одного измерения: ", (t2 - t1) / count, "Частота дискретизации: ",
          count / (t2 - t1), "Шаг квантования: ", 3.3 / 255)
    plt.plot(counter, arrdigitalU)         # Построение графика значения цифрового значения напряжения от номера отсчета
    plt.show()
finally:
    gpio.output(dac, 0)
    gpio.cleanup()
