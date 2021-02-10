import yfinance as yf 
import csv

comp=csv.reader(open('Tickers.csv'))

for c in comp:

    symbol=c[0]

    history_filename='{}.csv'.format(symbol)

    f=open(history_filename,'w',newline="")

    ticker=yf.Ticker(symbol)
    df=ticker.history(period='1y')

    f.write(df.to_csv())
    f.close()
print("Execution successful")