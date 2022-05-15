import pickle
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

def trying_to_predict_life(data):

    #data_new = [[10, 11, 0, 0, 0, 0, 12, 13, 14, 0]]
    cls2 = pickle.load(open('final_prediction.pickle', 'rb'))
    y_pred1 = cls2.predict(data)
    return y_pred1