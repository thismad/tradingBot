import requests
import json
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime,timedelta
from mpl_finance import candlestick_ohlc

url =  "https://api.binance.com"
actualTime = datetime.now()
startTime = (actualTime - timedelta(days=26)).timestamp()

params = {
    "symbol":"BTCUSDT",
    "limit":500,
    "interval":"4h",
    "startTime":startTime,
    "endTime":actualTime
}



repJson = requests.get(url+"/api/v3/klines", params=params)
print(repJson.json())
