from knock72 import remove_stopwords, word2num, stemmer, file_length
import re
import numpy as np
from sklearn.linear_model import LogisticRegression
import copy


y = []
phai = []
_phai = []
_y = []
# ああ、本当に頭が悪い...
i = 1
c = 0
with open("./sentiment.txt", "r") as fp:
    for line in fp:
        if c > i * file_length / 6:
            phai.append(_phai)
            y.append(_y)
            _phai = []
            _y = []
            i += 1

        score = int(line[:2:])
        line = re.sub("[\[\]]", "", line[3::])
        line = remove_stopwords(line)
        _y.append(score)
        phai_i = [0 for i in range(len(word2num))]
        for word in line.split(" "):
            word = stemmer.stemWord(word)
            if word in word2num:
                phai_i[word2num[word]] = 1
        _phai.append(phai_i)
        c += 1

y = np.asarray(y)
phai = np.asarray(phai)


def train_test_split(k):
    train_x = []
    train_y = []
    test_x = []
    test_y = []
    for i in range(y.shape[0]):
        if i == k:
            test_x = np.asarray(phai[i])
            test_y = np.asarray(y[i])
        else:
            train_x.append(np.asarray(phai[i]))
            train_y.append(np.asarray(y[i]))
    train_x = np.vstack(train_x)
    train_y = np.hstack(train_y)
    return train_x, train_y, test_x, test_y


# 最初から5分割することを見込んでコードを書かない自分の頭の悪さよ...

def score(model, train_x, train_y, test_x, test_y, threshold=0.5):
    model.fit(train_x, train_y)

    TP = 0
    FP = 0
    FN = 0
    TN = 0
    probs = model.predict_proba(test_x)
    for prob, score in zip(probs, test_y):
        if prob[0] < threshold:
            predict = +1
        else:
            predict = -1

        if score == +1 and predict == +1:
            TP += 1
        if score == +1 and predict == -1:
            FN += 1
        if score == -1 and predict == +1:
            FP += 1
        if score == -1 and predict == -1:
            TN += 1

    accuracy = (TP + TN) / (TP + FP + FN + TN)
    
    if TP + FP == 0:
        precision = 0
    else:
        precision = TP / (TP + FP)

    if TP + FN == 0:
        recall = 0
    else:
        recall = TP / (TP + FN)

    if recall + precision == 0:
        f1 = 0
    else:
        f1 = 2 * recall * precision / (recall + precision)

    return accuracy, precision, recall, f1


if __name__ == "__main__":
    for k in range(5):
        train_x, train_y, test_x, test_y = train_test_split(k)
        model = LogisticRegression()

        print('k:{0}\n正解率:{1}\n適合率:{2}\n再現率:{3}\nF1スコア:{4}'.format(
            k, *score(model, train_x, train_y, test_x, test_y)))
        print("----------")
