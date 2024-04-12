import keras

def predict(data):
    preprocess = keras.models.load_model("preprocessor.keras")
    data = preprocess(data)
    reg = keras.models.load_model("tensor_model.h5")
    return reg.predict(data)
