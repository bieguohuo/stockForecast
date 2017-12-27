# -*- coding: UTF-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split

features = ['kline - open',
            # 'kline - close', 'kline - low',
            # 'kline - amount',
            # 'kline - high',
            # 'kline - preClose',
            'kline - volume',
            'kline - netChangeRatio', 'ma5 - volume',
            # 'ma5 - avgPrice',
            'ma10 - volume',
            # 'ma10 - avgPrice',
            'ma20 - volume',
            # 'ma20 - avgPrice',
            'macd - diff', 'macd - macd', 'macd - dea', 'kdj - k', 'kdj - j',
            'kdj - d', 'rsi - rsi2', 'rsi - rsi3', 'rsi - rsi1', 'stock_name']
'''
features = ['kline - netChangeRatio', 'kdj - j', 'macd - macd', 'kline - open', ]
'''
stock_name = ['600000', '600029', '600048', '600104', '600547', '600887', '600999', '601166',
              '601198', '601288', '601336', '601601', '601688', '601800', '601988', '600016',
              '600030', '600050', '600111', '600518', '600606', '601006', '601169', '601211',
              '601318', '601390', '601628', '601766', '601818', '601901', '601989', '600028',
              '600036', '600100', '600340', '600519', '600837', '600958', '601088', '601186',
              '601328', '601398', '601668', '601788', '601857', '601985'
              ]

# 读取处理数据
x = []
''''''
for i in range(46):
    stock = pd.read_excel('./data/stockList.xls', sheet_name=[i])[i]
    stock['date'] = [str(j) for j in stock['date']]  # 将日期转为字符串格式
    stock['date'] = pd.to_datetime(stock['date'])  # 解析日期
    stock['stock_name'] = str(i)  # 加入股票编号
    del stock['kline - ccl']  # 删去无用的特征
    del stock['ma10 - ccl']
    del stock['ma20 - ccl']
    del stock['ma5 - ccl']
    del stock['event - type']
    del stock['event - desc']

    # del stock['']
    stock = stock[stock["date"] > "2015-12-31"]  # 只取16年的数据
    stockGroup = stock.groupby('stock_name', as_index=False).resample('1M', on='date').mean()  # 按月聚合
    stockGroup['stock_name'] = int(stock_name[i])  # 加入股票编号特征
    stockGroup = stockGroup[features]
    a = stockGroup
    x.append(stockGroup.values)
x = np.vstack(x)
print(a.columns)

labels = pd.read_excel('./data/labels.xlsx', sheet_name=[0])[0]
del labels['stock_name']
y = np.hstack(labels.values).reshape(-1, )
print(x.shape, y.shape)

train_x, test_x, train_y, test_y = train_test_split(x, y, test_size=0.2, random_state=1, stratify=y)
'''
# 网格搜索
model = xgb.XGBClassifier(max_depth=15, learning_rate=0.1, n_estimators=100)
param = {'max_depth':[5, 10, 15, 20], 'n_estimators':[50, 100, 150]}
gsearch = GridSearchCV(estimator=model, param_grid=param, cv=10)
gsearch.fit(train_x, train_y)
print("best_score:", gsearch.best_score_)
print("best_params:", gsearch.best_params_)
'''
model = xgb.XGBClassifier(learning_rate=0.1,
                          max_depth=10,  # gsearch.best_params_['max_depth'],
                          n_estimators=100,  # gsearch.best_params_['n_estimators'],
                          )
model.fit(train_x, train_y)
# prediction = model.predict(test_x)
print("test accuracy:", model.score(test_x, test_y))
xgb.plot_importance(booster=model)
print(model.feature_importances_)
plt.show()
