import matplotlib.pyplot as plt
from knock36 import count


frequency = [count[i][1] for i in range(10)]
word = [count[i][0] for i in range(10)]

x = [i for i in range(len(frequency))]

plt.bar(x, frequency)
plt.xticks(x, word)

plt.show()
# 名詞か動詞ランクインしろよ...
