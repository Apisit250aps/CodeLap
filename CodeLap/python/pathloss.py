import matplotlib.pyplot as plt
import numpy as np
from math import *


m = 100

list_24 = []
list_50 = []

for i in range(1, m+1):
    d0 = 3
    n = 2
    pathloss = (10*n*(log10((i/d0))))
    _24GHz = (20*log10(((4*pi*d0))/(0.13)))+pathloss
    _50GHz = ((20*log10(((4*pi*d0))/(0.06)))+pathloss)
    x2 = f"{20-_50GHz:.2f}"
    x1 = f"{20-_24GHz:.2f}"
    
    list_24.append(float(x1))
    list_50.append(float(x2))


y_1 = list_24
# print(y_1)
y_2 = list_50
# print(y_2)
x = np.arange(1, m+1)

plt.plot(x, y_1, 'rs-', label="2.4GHz")
plt.plot(x, y_2, 'gP:', label="5.0GHz")
plt.ylabel("dB")
plt.xlabel("Meter")
plt.legend(loc='best')
plt.show()