from knock73 import model
from knock72 import num2word
import numpy as np

prob = (-1) * np.sort((-1) * abs(model.coef_[0]))
print("--useful--")
for i in range(10):
    ind = np.where(abs(abs(model.coef_[0]) - prob[i]) < 1e-10)[0][0]
    print(num2word[ind])
print("--useless--")
# くそっ!重みが低い奴らはみんな0だ!
ind = np.where(model.coef_[0] == 0)[0][:10:]
for i in ind:
    print(num2word[i])


# stemmer, 仕事してるか?
