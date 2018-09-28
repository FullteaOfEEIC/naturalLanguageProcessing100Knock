import matplotlib.pyplot as plt
from knock36 import count

y = []
for i in count:
    y.append(i[1])

if __name__ == "__main__":
    plt.hist(y, bins=50, range=(0, 30))
    plt.show()
