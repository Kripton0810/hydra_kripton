import numpy as np
import sklearn 
import pandas as pd
from sklearn import tree
def fun(pm2,pm5,no,no2,nox,nh3,co,so2,o3,c6,tol,xy,aqi):
    dataset = pd.read_csv("city_day.csv")
    data = pd.DataFrame(dataset)
    X = data[['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene','AQI']]
    y = data['AQI_Bucket']

    clf = tree.DecisionTreeClassifier()
    X=X.fillna(0)
    y = y.fillna('no idea')
    clf = clf.fit(X, y)
    Xf=[[pm2,pm5,no,no2,nox,nh3,co,so2,o3,c6,tol,xy,aqi]]
    X1=[[12,60,4.10,100,20,0.00,1.50,40,30,3,10,2,40]]
    X2 =[[24.38,74.09,3.42,26.06,16.53,11.99,0.52,12.72,30.14,0.74,2.21,0.38,70.0]]
    return (clf.predict(Xf))
