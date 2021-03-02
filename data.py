import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import yfinance as yf
import datetime

#data = yf.download(tickers='UBER', period='1d', interval='1m')
#print(data.to_string())

import time

from polygon import WebSocketClient, STOCKS_CLUSTER
from polygon import RESTClient


def my_custom_process_message(message):
    print("this is my custom message processing", message)


def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")



def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = 'OPPbvGe36KYJppxXzHQftrYcPhCGNWYa'
    # Web Socket
    # my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_process_message)
    # my_client.run_async()
    #
    # my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    # time.sleep(1)
    #
    # my_client.close_connection()


    # Rest Client
    with RESTClient(key) as client:
        from_ = "2021-02-01"
        to = "2021-02-27"
        resp = client.stocks_equities_aggregates("AAPL", 1, "minute", from_, to, unadjusted=False)

        print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")


if __name__ == "__main__":
    main()
