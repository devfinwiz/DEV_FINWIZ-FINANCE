This is a finance repository that currently does the following:

1. Data fetching for Stocks listed on NSE India(CSVGenerator.py)
   1.1 -> List of tickers available (Tickers.csv)
   1.2 -> Garbage Collector is prepared to filter out delisted companies from the stock exchange(GarbageCollector.py)
2. CandleStick Pattern Recognition (talib.py,PatternRecognition.py)
3. Financials Data Extraction for basic fundamental analysis(FinancialsExtractor.py)
   3.1 -> Data set extracted available (Financials.csv)
4. Fundamental Screener to sort undervalued stocks(FundamentalScreener.py)
5. Mailer for sending the undervalued scanned stocks in csv file format(Mailer.py)
