from knock38 import y
import matplotlib.pyplot as plt

zipf = {}

for i in y:
    zipf[i] = zipf.get(i, 0) + 1

x = []
y = []
for key in zipf:
    x.append(key)
    y.append(zipf[key])


plt.plot(x, y)
plt.xscale("log")
plt.yscale("log")
plt.show()
