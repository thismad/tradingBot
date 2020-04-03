import requests
import json
import matplotlib.pyplot as plt
import matplotlib.dates as pltDate
import matplotlib.ticker as ticker
import numpy as np
import pandas as pd
from datetime import datetime,timedelta
from mpl_finance import candlestick_ohlc


actualTime = datetime.now()
startTime = int((actualTime - timedelta(days=26)).timestamp())
actualTime = int(actualTime.timestamp())



def requestUrl(symbol,interval):
    while not isinstance(symbol,str):
        symbol = input("type a valid symbol")
    url = "https://api.binance.com"
    params = {
        "symbol": symbol,
        "interval": interval,
    }
    rep = (requests.get(url + "/api/v3/klines", params=params))
    if rep.status_code ==200:
        print("it went successful!")
    rep = rep.json()
    df = pd.DataFrame(rep)
    df.columns = ['open_time',
                  'o', 'h', 'l', 'c', 'v',
                  'close_time', 'qav', 'num_trades',
                  'taker_base_vol', 'taker_quote_vol', 'ignore']
    types = {"o":"float", "h":"float", "l":"float", "c":"float", "v":"float"}
    df = df.astype(types)
    #df.index = [datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    df["open_time"] = [pltDate.date2num(datetime.fromtimestamp(x/1000)) for x in df["open_time"].values]
    quotes = [tuple(x) for x in df[["open_time","o","h","l","c"]].values]
    fig, ax = plt.subplots()
    candlestick_ohlc(ax, quotes, colorup="g", colordown="r")
    myFmt = pltDate.DateFormatter("%b %d")
    myMFmt = pltDate.DateFormatter("%h")
    ax.xaxis.set_major_formatter(myFmt)
    ax.xaxis.set_major_locator(ticker.MaxNLocator(10))
    ax.xaxis.set_minor_locator(pltDate.DayLocator())

    fig.autofmt_xdate()

    plt.show()



requestUrl("BTCUSDT","1d")
