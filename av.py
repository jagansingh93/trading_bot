import pandas as pd
from alpha_vantage.timeseries import TimeSeries
import time

api_key = '4JBCNFIKE9W82DZU'

ts = TimeSeries(key = api_key, output_format = 'pandas')
data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize = 'compact')
print(data)

# Try this when market is open
