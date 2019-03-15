from knock76 import label


TP = 0
FP = 0
FN = 0
TN = 0

for i in label():
    score, predict, prob = i
    if score == +1 and predict == +1:
        TP += 1
    if score == +1 and predict == -1:
        FN += 1
    if score == -1 and predict == +1:
        FP += 1
    if score == -1 and predict == -1:
        TN += 1

accuracy = (TP + TN) / (TP + FP + FN + TN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * recall * precision / (recall + precision)
print('正解率:{0}\n適合率:{1}\n再現率:{2}\nF1スコア:{3}'.format(
    accuracy, precision, recall, f1
))
