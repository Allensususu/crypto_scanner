import numpy as np
import pandas as pd
import finlab_crypto
import time 
from finlab_crypto import Strategy
import datetime
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import xlwings as xw
import os
import matplotlib
import mplfinance as mpf

api_key = ""
api_secret = ""
finlab_crypto.setup()


client = Client(api_key, api_secret)
ticker = []
match_filter_ticker = []
match_filter = 0

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
               "USDCUSDT" not in p["symbol"] and
               "USDPUSDT" not in p["symbol"]):
                ticker.append(p["symbol"])

def show_klines(ticker):
    for q in ticker:
        df = pd.read_csv(f'./history/{q}-1d-data.csv', parse_dates=True, index_col=0) 
        df = df[-200:]
        mc = mpf.make_marketcolors(up='r',down='g',inherit=True)
        s  = mpf.make_mpf_style(base_mpf_style='binance',marketcolors=mc)
        kwargs = dict(type='candle', mav=(5,20,60), volume=True, figratio=(20,10), figscale=1, title=q, style=s) 
        if not os.path.isdir (f'./match_filter/{datetime.date.today()}'):
            os.mkdir(f'./match_filter/{datetime.date.today()}')
        mpf.plot(df, **kwargs,  savefig= f'./match_filter/{datetime.date.today()}/{q}.png')

list_get_usdt_ticker()

for p in ticker:
    ohlcv = finlab_crypto.crawler.get_all_binance(p, '1d')
    date = ohlcv.index  
    close = ohlcv.close
    low =  ohlcv.low 
    high =  ohlcv.high
    vol =  ohlcv.volume 
    
    if date[-1] != datetime.date.today():
        continue
        #pass
    #total_currency += 1

    if close[-1] > close.rolling(200).mean()[-1]:
        match_filter_ticker.append(p)
        

show_klines(match_filter_ticker)
#sheet.range('a:a').api.Insert()

#sheet1 = wb.sheets["sheet1"]

#print(get_all_history("DOGEUSDT"))
