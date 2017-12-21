import datetime as dt
import csv
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
from sklearn import datasets, linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.cross_validation import train_test_split
dates,prices=[],[]

def getdata(n,x):

    #start = dt.datetime(int(input('Enter year to start: ')), int(input('Start month: ')), int(input('Start date: ')))
    #end = dt.datetime(int(input('Enter year to end: ')), int(input('End month: ')), int(input('End date: ')))

    start = dt.datetime(2017,1,1) #test
    end = dt.datetime(2017,12,20) #test

    #df = web.DataReader(n, "yahoo", start, end).to_csv("aapl.csv") #data frame
    df = pd.read_csv('aapl.csv') #test

    global dates,prices

    de = df['Date'].values
    ye = df['Close'].values
    d = []
    for a in de:
        d.append(int(a.split('-')[0]))

    dates = np.array(d)
    prices = ye
    dates = np.reshape(dates, (len(dates),1)) # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices),1))

    #da_train,pr_train,da_test,pr_test = train_test_split(dates,prices,test_size =0.2,random_state =4)
    #reg = linear_model.LinearRegression().fit(da_train[:len(pr_train)],pr_train)
    #print(reg.score(da_test[:len(pr_test)],pr_test))
    
    

#getdata(input('Enter Company Name to Display(eg APPLE: AAPL): ').upper())
print(getdata('aapl',2017)) #test
