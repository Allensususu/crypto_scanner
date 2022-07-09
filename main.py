import numpy as np
import pandas as pd
import finlab_crypto
import time 
from finlab_crypto import Strategy
import datetime
from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager
import xlwings as xw
import os

api_key = ""
api_secret = ""
finlab_crypto.setup()


client = Client(api_key, api_secret)
ticker = []
match_filter_ticker = []
total_20MA = 0
above_20MA = 0
above_20MA_list = []
total_50MA = 0
above_50MA = 0
above_50MA_list = []
total_200MA = 0
above_200MA = 0
above_200MA_list = []
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


ohlcv = finlab_crypto.crawler.get_all_binance("ETHUSDT", '1d')
close = ohlcv.close
date = ohlcv.index  
low =  ohlcv.low 


list_get_usdt_ticker()

for p in ticker:
    ohlcv = finlab_crypto.crawler.get_all_binance(p, '1d')
    close = ohlcv.close
    date = ohlcv.index    
    if date[-1] != datetime.date.today():
        continue
        #pass
    #total_currency += 1

    if len(ohlcv) > 20 :
        total_20MA += 1 
        if close[-1] > close.rolling(20).mean()[-1]:
            above_20MA += 1
    if len(ohlcv) > 50 :
        total_50MA += 1 
        if close[-1] > close.rolling(50).mean()[-1]:
            above_50MA += 1
            above_50MA_list.append(p)
    if len(ohlcv) > 200 :
        total_200MA += 1 
        if close[-1] > close.rolling(200).mean()[-1]:
            above_200MA += 1
            above_200MA_list.append(p)

    ###篩選
    if len(ohlcv) > 50 :
        if ((close[-1] > close.rolling(20).mean()[-1]) and 
            (close[-1] > close.rolling(50).mean()[-1]) and
            (close.rolling(20).mean()[-1] > close.rolling(50).mean()[-1]) and
            ((close[-1] > (low.rolling(50).min()[-1]*1.7)))):
            match_filter += 1
            match_filter_ticker.append(p)
    else :
        if ((close[-1] > close.rolling(int(len(ohlcv)/3)).mean()[-1]) and 
            (close[-1] > close.rolling(int(len(ohlcv)/3*2)).mean()[-1]) and
            (close.rolling(int(len(ohlcv)/3)).mean()[-1] > close.rolling(int(len(ohlcv)/3*2)).mean()[-1]) and
            ((close[-1] > (low.rolling(int(len(ohlcv)/3*2)).min()[-1]*1.7)))):
            match_filter += 1
            match_filter_ticker.append(p)



if not os.path.isfile( datetime.date.today().year +"_crypto.xlsx" ):
    app=xw.App(visible=False,add_book=False)
    wb=app.books.add()
    wb.save( datetime.date.today().year +"_crypto.xlsx" )
    wb.close()
    app.quit()
app=xw.App(visible=True,add_book=False)
#app.display_alerts=False 
#app.screen_updating=False  
wb=app.books.open(datetime.date.today().year +"_crypto.xlsx")
#time.sleep(3)

sheet = wb.sheets["工作表1"]
if sheet.range('B1').value != datetime.date.today() :
    sheet.range('b:b').api.Insert()
    sheet.range('B1').value = datetime.date.today()
    sheet.range('B3').value = above_20MA
    sheet.range('B4').value = (' {:.2%}'.format(above_20MA / total_20MA))
    sheet.range('B6').value = above_50MA
    sheet.range('B7').value = (' {:.2%}'.format(above_50MA / total_50MA))
    sheet.range('B9').value = above_200MA
    sheet.range('B10').value = (' {:.2%}'.format(above_200MA / total_200MA))
    sheet.range('B12').value = match_filter


print(above_50MA_list )
print(above_200MA_list )
#sheet.range('a:a').api.Insert()

#sheet1 = wb.sheets["sheet1"]

#print(get_all_history("DOGEUSDT"))
