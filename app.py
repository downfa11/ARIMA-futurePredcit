import pybithumb
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima.model import ARIMA
import datetime

dd = pybithumb.get_ohlcv("BTC")
df = dd.tz_localize(None)
df.reset_index(inplace=True)

# 5일전의 날짜
train_date = datetime.datetime.now() - datetime.timedelta(days=5)
print(train_date)
# 현재 날짜
test_date = datetime.datetime.now()

train = df.loc[df['time'] <= train_date]
test = df.loc[df['time'].dt.date == test_date.date()]

model = ARIMA(train['close'].values, order=(0, 1, 1))
model_fit = model.fit()

forecast = model_fit.forecast(steps=5)

pred_y = forecast[0].tolist()
test_y = test['close'].values.tolist()

print(f"Predicted price after 5 days: {pred_y}")
print(f"Actual price: {test_y}")