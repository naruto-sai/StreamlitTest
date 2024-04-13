import pickle
def predict(data):
    reg = pickle.load(open('xgb_tune.pkl','rb'))
    return reg.predict(data)
