import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math

fig = plt.figure()

data = np.loadtxt(r"C:\Users\andre\Downloads\data.txt")
settings = np.loadtxt(r"C:\Users\andre\Downloads\settings.txt")

step = settings[1]
t = 1/settings[0]


data = data[:len(data)-1] * step
time = np.zeros(len(data), dtype=float)
datap = np.zeros(len(data) // 5)
timep = np.zeros(len(time)//5)
m = np.max(data)
for i in range(len(data)):
    time[i] = i * t
    if data[i] == m:
        tCharge = round(time[i], 2)
for i in range(len(datap)):
    datap[i] = data[5*i]
    timep[i] = time[5*i]



ax = plt.axes([0.1, 0.1, 0.8, 0.8])
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5, 0.0))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.1, 0.0))
ax.set_title("Процесс заряда и разряда конденсатора в RC-цепочке")
ax.set_ylabel("Напряжение, В")
ax.set_xlabel("Время, с")
ax.grid(visible=True, which='minor', linestyle='dashed', linewidth=0.5)
ax.grid(visible=True, which='major')
ax.set_xlim(0, math.trunc(np.max(time))+1)
ax.set_ylim(0, math.trunc(np.max(data))+1)



ax.plot(timep, datap, 'o-', color='blue', label='V(t)')
string = "Время заряда: " + str(tCharge) + " с"
plt.text(10, 2, string)
ax.legend()
plt.savefig('grafik.svg')
plt.show()







