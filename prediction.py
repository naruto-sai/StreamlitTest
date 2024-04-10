import joblib as jb
def predict(data):
    clf = jb.load("iris_classifier_model.sav")
    return clf.predict(data)
