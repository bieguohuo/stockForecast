import numpy as np
import pandas as pd
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from keras.initializers import he_uniform
from keras.layers import LSTM, Dense
from keras.models import Sequential
from keras.optimizers import Adam
from sklearn.preprocessing import MinMaxScaler

min_max = MinMaxScaler(feature_range=(0, 1))
# 读取数据
stock = pd.read_excel('stockList2017-class.xls', sheet_name=[0])[0]

# 删去无用的特征
del stock['date']
del stock['kline - ccl']
del stock['ma10 - ccl']
del stock['ma20 - ccl']
del stock['ma5 - ccl']
del stock['event - type']
del stock['event - desc']

time_steps = 80
# 提取数据
data = stock.values[:-5, :]
print("data shape:", data.shape)  # 443,24
# plt.plot(data[:, 23])
# plt.show()
X = min_max.fit_transform(data[:, :-1])
print(X)
# 标签
labels = np.array([data[i, -1] for i in range(443 - time_steps - 5)])
print("labels shape:", labels.shape)
# 特征
x = np.array([X[i: i + time_steps, :] for i in range(5, 443 - time_steps)])
print("x shape:", x.shape)

# 建立模型
model = Sequential()

model.add(LSTM(input_shape=(time_steps, 23),
               units=512,
               activation='relu',
               kernel_initializer=he_uniform(seed=2),
               # dropout=0.5,
               return_sequences=True,
               ))
model.add(LSTM(
    units=512,
    activation='relu',
    kernel_initializer=he_uniform(seed=2),
    # dropout=0.5,
))
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# 训练
adam = Adam(0.00001)
model.compile(optimizer=adam, loss='binary_crossentropy', metrics=['accuracy'])
early = EarlyStopping(monitor='val_acc', min_delta=0, patience=15, verbose=1, mode='min')
reduce_lr_loss = ReduceLROnPlateau(monitor='val_acc', factor=0.1, patience=12, verbose=1, epsilon=1e-4, mode='min')
model.fit(x, labels, batch_size=32, epochs=500, verbose=1,
          callbacks=[early, reduce_lr_loss],
          validation_split=0.2,
          )
