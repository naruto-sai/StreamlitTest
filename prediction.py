import joblib as jb
def predict(data):
    reg = jb.load("xgb_tune.sav")
    return reg.predict(data)
