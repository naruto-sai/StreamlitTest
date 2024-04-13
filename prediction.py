import pickle
def predict(data):
    reg = pickle.load(open('xgb_tune_1.pkl','rb'))
    return reg.predict(data)
