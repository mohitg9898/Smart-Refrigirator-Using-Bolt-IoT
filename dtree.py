# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import recall_score, precision_score
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split


def MachineLearning_model(ldr_value):

    dataset = pd.read_csv("sensorvalues.csv")

    state_lb = LabelBinarizer()
    Y = state_lb.fit_transform(dataset.state.values)
    FEATURES = dataset.columns[0]
    X_data = np.asarray(dataset[FEATURES])
    X_data = X_data.reshape(-1, 1)
    X_train, X_test, y_train, y_test = train_test_split(X_data, Y, test_size=0.3, random_state=1)
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
   
    pred = clf.predict(X_test)
    precision = precision_score(y_test, pred, average="weighted")
    recall = recall_score(y_test, pred, average="weighted")
    state = clf.predict(np.array([ldr_value]).reshape(-1, 1))
    return state

