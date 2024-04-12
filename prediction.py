import joblib as jb
# import tensorflow as tf
def predict(data):
    preprocess = jb.load("preprocessor.sav")
    tensor_data = preprocess(data)
    reg = jb.load("tensor_model.sav")
    return reg.predict(tensor_data)
