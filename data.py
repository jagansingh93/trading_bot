import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf


data = yf.download(tickers='UBER', period='1d', interval='1m')
print(data.to_string())
