import joblib as jb

def predict(data):
    preprocess = jb.load("preprocessor.sav")
    data = preprocess(data)
    reg = jb.load("tensor_model.sav")
    return reg.predict(data)
