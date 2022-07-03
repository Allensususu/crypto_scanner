import numpy as np
import pandas as pd
import finlab_crypto
import time 
from finlab_crypto import Strategy
import datetime

api_key = "J0gq06B1YlsLVPfkkJ3LAEPHMOwQ74EaUGXiDBEyCiGIkRuDJAZz95RThMFmgyyc"
api_secret = "9L828724dXaEB6z0V91b5GoodFdmP93qMe9vExUHI4eTv4dx0ozWCl4wSrvavId9"
finlab_crypto.setup()
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(api_key, api_secret)
ticker = []

total_currency = 0
above_20MA = 0
above_50MA = 0
above_200MA = 0

def list_get_usdt_ticker():
    for p in client.get_all_tickers() :
        if p["symbol"][-4:] == "USDT":
            if ("DOWN" not in  p["symbol"] and 
               "UPUSDT" not in p["symbol"] and 
               "AUDUSDT" not in p["symbol"] and 
               "UPUSDT" not in p["symbol"] and 
               "EURUSDT" not in p["symbol"] and 
               "GPBUSDT" not in p["symbol"] and 
               "BUSDUSDT" not in p["symbol"] and 
               "TUSDUSDT" not in p["symbol"] and 
               "BULL" not in p["symbol"] and
               "USDCUSDT" not in p["symbol"] ):
                ticker.append(p["symbol"])

list_get_usdt_ticker()
for p in ticker:
    ohlcv = finlab_crypto.crawler.get_all_binance(p, '1d')
    close = ohlcv.close
    date = ohlcv.index    
    if date[-1] != datetime.date.today():
        continue
        #pass

    #total_currency += 1
 
    """
    if (len(ohlcv)) > 200 :
        if close[-1] > close.rolling(20).mean()[-1]:
            above_20MA += 1
        if close[-1] > close.rolling(50).mean()[-1]:
            above_50MA += 1
        if close[-1] > close.rolling(200).mean()[-1]:
            above_200MA += 1
    else if:
        if close[-1] > close.rolling(10).mean()[-1]:
            above_20MA += 1
        if close[-1] > close.rolling(int(len(ohlcv)/3)).mean()[-1]:
            above_50MA += 1
        if close[-1] > close.rolling(int(len(ohlcv)/3*2)).mean()[-1]:
            above_200MA += 1
            """
    if close[-1] > close.rolling(20).mean()[-1]:
        above_20MA += 1
    if close[-1] > close.rolling(50).mean()[-1]:
        above_50MA += 1
    if close[-1] > close.rolling(200).mean()[-1]:
        above_200MA += 1
        

total_currency = 0
print(total_currency)
print(above_20MA)
print(above_50MA)
print(above_200MA)

#print(get_all_history("DOGEUSDT"))