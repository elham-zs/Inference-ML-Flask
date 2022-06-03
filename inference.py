import pickle
from flask import Flask
from flask import request
import numpy as np
import json
import os


def load_classifier():
    with open("iris_classifier", "rb") as f:
        clf = pickle.load(f)

    with open("feature_names", "rb") as f:
        features = pickle.load(f)

    return clf, features


clf, features = load_classifier()
class_name = ['setosa', 'versicolor', 'virginica']

app = Flask(__name__)
port = int(os.getenv('PORT', '5000'))


@app.route('/predict', methods=['POST'])
def inference():
    resp = {}

    content = request.json
    if not isinstance(content, list):
        content = [content]

    for i, elem in enumerate(content):
        test_data = []
        for feature in features:
            test_data.append(elem[feature])
        species = clf.predict(np.array([test_data]))
        resp.update({"input {}".format(i):class_name[species[0]]})
#     print("done")

    return json.dumps(resp, indent=4)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
