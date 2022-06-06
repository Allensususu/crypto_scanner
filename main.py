import numpy as np
import pandas as pd

import time 

api_key = "GmevgkkgrESSGDmgXqSK0jp5m2zct0qSsxnz1ASJuxX1QpZk8rw9Pc5n98wuEHIk"
api_secret = "cEyywXGpBaTqUZl7y4poQW6m6NjRqV0nmQjz4I306fwPNFTuwu595r4k9ALwW970"

from binance import Client, ThreadedWebsocketManager, ThreadedDepthCacheManager

client = Client(api_key, api_secret)

def list_get_usdt_ticker():
    for p in client.get_all_tickers() :
        if p["symbol"][-4:] == "USDT":
            print (p["symbol"]) 

def get_all_history(ticker):
    klines = client.get_historical_klines(ticker , Client.KLINE_INTERVAL_1MINUTE  ,"1 Jan, 2022")
    #print(klines)
    df = pd.DataFrame(klines)
    df.columns = ["Time" , "Open", "Close" , "High","Low","Volume","useless1","useless2","useless3","useless4","useless5","useless6"]
    df = df.drop (["useless1","useless2","useless3","useless4","useless5","useless6"], axis =1)
    return df

#list_get_usdt_ticker()
print(get_all_history("DOGEUSDT"))