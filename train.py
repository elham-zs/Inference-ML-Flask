from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import pickle


def train():
    # load data
    iris_dataset = load_iris()
    # show iris data https://www.kaggle.com/uciml/iris

    data = iris_dataset["data"]
    feature_names = iris_dataset["feature_names"]
    target = iris_dataset["target"]
    target_names = iris_dataset["target_names"]

    print("Target names: {}".format(target_names))
    print("Feature names: {}".format(feature_names))
    print("Type of data: {}".format(type(data)))
    print("Shape of data: {}".format(data.shape))

    print("Type of target: {}".format(type(target)))
    print("Shape of target: {}".format(target.shape))
    print("Target:\n{}".format(target))

    # split training data
    X_train, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2)

    print("X_train shape: {}".format(X_train.shape))
    print("y_train shape: {}".format(y_train.shape))

    # train model
    clf = LogisticRegression(solver='liblinear', multi_class='auto', max_iter=1000)
    clf.fit(X_train, y_train)

    # validate model
    y_test_pred = clf.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_test_pred)

    print(f"accuracy on test data {test_accuracy}")

    test(clf, target_names)

    # save classifier
    with open("iris_classifier", "wb") as f:
        pickle.dump(clf, f)

    with open("feature_names", "wb") as f:
        pickle.dump(feature_names, f)


def test(clf, class_name):
    new_iris_setosa = np.array([[5, 2.9, 1, 0.2]])
    new_iris_virginica = np.array([[5.8, 2.7, 5.1, 1.9]])
    new_iris_versicolor = np.array([[5.5, 2.5, 4.0, 1.3]])

    test_data = [new_iris_setosa, new_iris_virginica, new_iris_versicolor]
    for data in test_data:
        preds = clf.predict(data)
        print(f"predict {class_name[preds]}")


if __name__ == "__main__":
    train()