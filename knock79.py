from knock78 import train_test_split, score
from sklearn.linear_model import LogisticRegression
try:
    from tqdm import tqdm
except:
    def tqdm(iter):
        return iter
import matplotlib.pyplot as plt

if __name__ == "__main__":

    thresholds=[]
    accuracies=[]
    precisions=[]
    recalls=[]
    f1s=[]

    for _threshold in tqdm(range(101)):
        threshold = _threshold / 100
        accuracy = 0
        precision = 0
        recall = 0
        f1 = 0
        for k in range(5):
            train_x, train_y, test_x, test_y = train_test_split(k)
            model = LogisticRegression(solver="liblinear")

            _accuracy, _precision, _recall, _f1 = score(
                model, train_x, train_y, test_x, test_y, threshold=threshold)
            accuracy += _accuracy
            precision += _precision
            recall += _recall
            f1 += _f1

        accuracy = accuracy / 5
        precision = precision / 5
        recall = recall / 5
        f1 = f1 / 5
        thresholds.append(threshold)
        accuracies.append(accuracy)
        precisions.append(precision)
        recalls.append(recall)
        f1s.append(f1)

    plt.plot(thresholds,accuracies,label="accuracy")
    plt.plot(thresholds,precisions,label="precision")
    plt.plot(thresholds,recalls,label="recall")
    plt.plot(thresholds,f1s,label="f1")
    plt.legend()
    plt.show()
