import joblib as jb
def predict(data):
    clf = jb.load("iris_classifier_model.sav")
    print(clf.predict(data))
    return clf.predict(data)