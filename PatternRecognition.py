import csv
import talib
import numpy

def is_bullish_candlestick(candle):
    return float(candle['Close']>candle['Open'])

def is_bearish_candlestick(candle):
    return float(candle['Close']<candle['Open'])

def is_bullish_engulfing(candles,index):
    current_day=candles[index]
    previous_day=candles[index-1]
    
    if is_bearish_candlestick(previous_day) \
        and float(current_day['High'])>float(previous_day['Close']) \
        and float(current_day['Close'])>float(previous_day['Open']) \
        and float(current_day['Open'])<float(previous_day['Close']):
        return True

    return False

def is_bearish_engulfing(candles,index):
    current_day=candles[index]
    previous_day=candles[index-1]
    
    if is_bullish_candlestick(previous_day) \
        and float(current_day['Close'])<float(previous_day['Low'])\
        and float(current_day['Open'])>float(previous_day['High']):
        return True

    return False

def is_gravestone_doji(candles,index):
    current_day=candles[index]
    previous_day=candles[index-1]

    if is_bullish_candlestick(previous_day) \
        and float(current_day['High'])>float(previous_day['High'])\
        and float(current_day['Open'])>float(previous_day['Close'])\
        and float(current_day['Open'])==float(current_day['Low']) \
        and float(current_day['Close'])<=float(current_day['Open']):
        return True

    return False

def pattern_recognition(candles,index):
    current_day=candles[index]

    open=current_day['Open']
    high=current_day['High']
    low=current_day['Low']
    close=current_day['Close']

    open=numpy.array(open,dtype=float)
    high=numpy.array(high,dtype=float)
    low=numpy.array(low,dtype=float)
    close=numpy.array(close,dtype=float)
    
    
    #result=talib.CDLDOJI(open,high,low,close)
    #print(result)

symbols_file=open('Symbols')
tickers=csv.reader(symbols_file)

for company in tickers:
    #print(company)

    ticker=company[0]

    history_file=open('{}'.format(ticker))

    reader=csv.DictReader(history_file)
    candles=list(reader)

    candles=candles[-2:]

    if len(candles)>1:
        if is_bullish_engulfing(candles,1):
            print("{} = {} is bullish engulfing".format(ticker,candles[1]['Date']))
            print("------------------------------------------------")

        if is_bearish_engulfing(candles,1):
            print("{} = {} is bearish engulfing".format(ticker,candles[1]['Date']))
            print("------------------------------------------------")

        if is_gravestone_doji(candles,1):
            print("{} = {} is gravestone doji".format(ticker,candles[1]['Date']))
            print("------------------------------------------------")

        #pattern_recognition(candles,1)
    
