# crypto_scanner
Get data on all USDT trading pairs on Binance, filter cryptocurrencies in a simple way, and draw the candlestick chart.

## How to use?
You can use the opening price, closing price, high and low price, and volume captured by the program to quickly filter cryptocurrencies.

```python
ohlcv = finlab_crypto.crawler.get_all_binance(ETHUSDT, '1d')
    date = ohlcv.index  
    close = ohlcv.close
    low =  ohlcv.low 
    high =  ohlcv.high
    vol =  ohlcv.volume 
```
Don't worry, the program will help you get all USDT trading pairs, this is just a demonstration.

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
```p
![123](https://user-images.githubusercontent.com/46346226/178109724-800304ba-21be-4921-8ce0-4d8d923d3327.PNG)
![456](https://user-images.githubusercontent.com/46346226/178109742-8dcd6067-5791-48ea-8d2a-58186555fdab.PNG)
