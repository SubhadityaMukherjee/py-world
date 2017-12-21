def getdata(n):
    import datetime as dt
    #start = dt.datetime(int(input('Enter year to start: ')), int(input('Start month: ')), int(input('Start date: '))) 
    #end = dt.datetime(int(input('Enter year to end: ')), int(input('End month: ')), int(input('End date: ')))
    
    start = dt.datetime(2000,1,1) #test
    end = dt.datetime(2017,12,20) #test
    
    import matplotlib.pyplot as plt
    from matplotlib import style
    import pandas as pd
    import pandas_datareader.data as web
    
    #df = web.DataReader(n, "yahoo", start, end) #data frame
    df = pd.read_csv('appl.csv') #test
    #print(df.head)
    
    from sklearn import datasets, linear_model
    from sklearn.preprocessing import PolynomialFeatures
    import numpy as np
    
    
    de = df['Date'].values
    d = []
    for a in de:
        d.append(int(a.split('-')[0]))
    ye = df['Adj Close'].values
    d = np.array(d,dtype = np.uint64).reshape(-1,1)
    ye = ye.reshape(-1,1)
    
    reg = linear_model.LinearRegression(fit_intercept=True, normalize=False).fit(d,ye)
    
    plt.plot(d, ye,  color='red')
    plt.plot(d, reg.predict(d), color='blue', linewidth=1)
    plt.xlabel('Time')
    plt.ylabel('Value in Dollar')
    plt.show()

    
    #style.use('ggplot')
    #df['Adj Close'].plot() #Create plot
    #plt.show() #Display plot

    return df # get data frame
#getdata(input('Enter Company Name to Display(eg APPLE: AAPL): ').upper())
getdata('aapl') #test
