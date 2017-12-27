# coding: utf-8

# In[1]:

import pandas as pd

# In[2]:

stock = pd.read_excel('stock.xls', sheet_name=[0])[0]

# In[4]:

print stock.head()

# In[ ]:



# In[5]:

stock.rename(columns={'kline - open': 'Open', 'kline - high': 'High', 'kline - low': 'Low', 'kline - close': 'Close',
                      'kline - volume': 'Volume'}, inplace=True)

# In[6]:

print stock.head()

# In[7]:

df = stock[['Open', 'High', 'Low', 'Close', 'Volume']]

# In[8]:

print df.head()

# In[9]:

print len(df
          )

# In[10]:

forecast_col = 'Close'

# In[11]:

df.fillna(value=99999, inplace=True)

# In[13]:

import math

forecast_out = int(math.ceil(0.01 * len(df)))

# In[14]:

print forecast_col

# In[15]:

print forecast_out

# In[16]:

df['label'] = df[forecast_col].shift(-forecast_out)

# In[17]:

print(df.shape)

# In[18]:

print(df.tail())

# In[24]:

import numpy as np

X = np.array(df.drop(['label'], 1))
print X

# In[ ]:




# In[22]:

from sklearn import preprocessing, cross_validation

X = preprocessing.scale(X)

# In[23]:

print X

# In[25]:

X_lately = X[-forecast_out:]

# In[26]:

print X_lately

# In[27]:

X = X[:-forecast_out]

# In[28]:

print X

# In[29]:

df.dropna(inplace=True)

# In[30]:

y = np.array(df['label'])

# In[31]:

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)

# In[32]:

from sklearn.linear_model import LinearRegression

# In[33]:

clf = LinearRegression()
clf.fit(X_train, y_train)

# In[34]:

accuracy = clf.score(X_test, y_test)

# In[35]:

print accuracy

# In[36]:

forecast_set = clf.predict(X_lately)

# In[37]:

print(forecast_set, accuracy, forecast_out)

# In[38]:

from matplotlib import style

# In[39]:

style.use('ggplot')

# In[40]:

df['Forecast'] = np.nan

# In[46]:

last_date = df.iloc[-2].name

# In[ ]:




# In[47]:

print last_date

# In[ ]:




# In[45]:

last_unix = last_date.timestamp()
