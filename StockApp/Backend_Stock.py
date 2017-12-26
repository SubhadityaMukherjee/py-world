import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from datetime import datetime
import datetime
import pandas_datareader.data as web

dates = []
prices = []

csvname = ''

def getfromserver(n):
    start = datetime.datetime(2017,12,1) #test
    end = datetime.datetime(2017,12,24) #testtest
    print("Checking between ",start,' and ',end)

    df = web.DataReader(n, "yahoo", start, end).to_csv("temp.csv") #data frame


def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader) # skipping column names
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            #prices.append(float(row[5])) #check adj close- not really accurate
            prices.append(float(row[1]))
    return

def predict_price(dates, prices, x):
    dates = np.reshape(dates, (len(dates),1)) # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices),1))
    
    linear_mod = linear_model.LinearRegression() # defining the linear regression model
    linear_mod.fit(dates, prices) # fitting the data points in the model
    plt.scatter(dates, prices, color= 'black', label= 'Data') # plotting the initial datapoints 
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Linear Regression')
    plt.legend()
    plt.show()
    
    return linear_mod.predict(x)[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]
getfromserver(input('Enter company name as per market: ').upper())
get_data('temp.csv') # calling get_data method by passing the csv file to it
x = int(input('Enter date in this month you want to check for: '))
predicted_price, coefficient, constant = predict_price(dates, prices, x)  
print("\nThe stock open price for ",x, "2is: $", str(predicted_price))
