def getdata(n):
	import datetime as dt
	start = dt.datetime(int(input('Enter year to start: ')), int(input('Start month: ')), int(input('Start date: '))) 
	end = dt.datetime(int(input('Enter year to end: ')), int(input('End month: ')), int(input('End date: ')))

	
	import matplotlib.pyplot as plt
	from matplotlib import style
	import pandas as pd
	import pandas_datareader.data as web
	
	df = web.DataReader(n, "yahoo", start, end) #data frame
	print(df.head())
	style.use('ggplot')
	df['Adj Close'].plot() #Create plot
	plt.show()	#Display plot

	return df # get data frame

getdata(input('Enter Company Name to Display(eg APPLE: AAPL): ').upper())
