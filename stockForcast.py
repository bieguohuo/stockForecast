# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 20:18:17 2016
@author: Jian
"""
import datetime

import numpy as np
import pandas as pd

# import pandas.io.data as web
import math
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import preprocessing, cross_validation
from sklearn.linear_model import LinearRegression

# 从互联网获取数据
# df = web.DataReader("XOM", "yahoo", start, end)
df = pd.read_excel('./data/stock.xls', sheet_name=[0])[0]
# print(df.head())
df.rename(columns={'kline - open': 'Open', 'kline - high': 'High', 'kline - low': 'Low', 'kline - close': 'Close',
                   'kline - volume': 'Volume'}, inplace=True)
df = df[['date', 'Open', 'High', 'Low', 'Close', 'Volume']]
df['HL_PCT'] = (df['High'] - df['Low']) / df['Close'] * 100.0
df['PCT_change'] = (df['Close'] - df['Open']) / df['Open'] * 100.0
df = df[['date', 'Close', 'HL_PCT', 'PCT_change', 'Volume']]
# print(df.head())
print(len(df))
forecast_col = 'Close'
df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))
# 预测forecast_out天后的
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)

print(df.shape)
print(df.tail())
X = np.array(df.drop(['label'], 1))

X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
print(X)
print(X_lately)
y = np.array(df['label'])
# print(y)
print(X.shape)
print(y.shape)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast_out)

style.use('ggplot')

df['Forecast'] = np.nan
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d', errors='ignore')

last_date = df['date'].name
last_unix = df['date'][0].timestamp()
print(last_date, last_unix)
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns) - 1)] + [i]
print(df.tail())

df['Close'].plot()
df['Forecast'].plot()
plt.show()

