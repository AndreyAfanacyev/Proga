import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('prices.csv', delimiter=',')
x, y = data[:,1], data[:,2]

x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

f1p, residuals, rank, sv, rcond = np.polyfit(x, y, 1, full=True)
f1 = np.poly1d(f1p)
fx = np.linspace(min(x), max(x), 500)

plt.scatter(x, y,)
plt.plot(fx, f1(fx), linewidth=1.0, color='r')
plt.title('Зависимость стоимости квартиры от её площади')
plt.xlabel('Площадь')
plt.ylabel('Стоимость')
plt.grid(True)
plt.show()

f2p, residuals, rank, sv, rcond = np.polyfit(x, y, 2, full=True)
f2 = np.poly1d(f1p)
fx = np.linspace(min(x), max(x), 500)

plt.scatter(x, y)
plt.plot(fx, f1(fx), linewidth=1.0, color='r')
plt.title('Зависимость стоимости квартиры от её площади')
plt.xlabel('Площадь')
plt.ylabel('Стоимость')
plt.grid(True)
plt.show()
