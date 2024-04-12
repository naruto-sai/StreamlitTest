import joblib as jb
import xgboost
def predict(data):
    reg = jb.load("xgb_tune.sav")
    return reg.predict(data)
