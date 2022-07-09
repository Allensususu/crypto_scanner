# crypto_scanner
Get data on all USDT trading pairs on Binance, filter cryptocurrencies in a simple way, and draw the candlestick chart.

## How to use?
Put in binance API first 
```python 
api_key = ""
api_secret = ""
```
And You can use the opening price, closing price, high and low price, and volume captured by the program to quickly filter cryptocurrencies.

```python 
ohlcv = finlab_crypto.crawler.get_all_binance(ETHUSDT, '1d')
    date = ohlcv.index  
    close = ohlcv.close
    low =  ohlcv.low 
    high =  ohlcv.high
    vol =  ohlcv.volume 
```
Don't worry, the program will via ```python list_get_usdt_ticker()``` help you get all USDT trading pairs, this is just a demonstration.

## Example 


```python
if close[-1] > close.rolling(200).mean()[-1]:
    match_filter_ticker.append(p)
```
You can use the rolling function to get the 200-day moving average, and a simple judgment formula can filter out the 200-day online cryptocurrency

## Save and plot

If all is done, you can call show_klines and it will save it in the match_filter folder for you
```python
show_klines(match_filter_ticker)
```


