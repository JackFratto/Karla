import yfinance as yf

if __name__ == "__main__":

    sp500 = yf.Ticker('^GSPC')
    black_berry = yf.Ticker('BB')
    home_depot = yf.Ticker('HD')
    gold_futures = yf.Ticker('GC=F')



    # Small Market Cap Stocks
    black_berry.history().to_csv('data/small_mkt_cap/bb.csv', index=False) 

    # S&P 500 Stocks
    sp500.history().to_csv('data/sp500/sp500.csv', index=False)
    home_depot.history().to_csv('data/sp500/hd.csv', index=False)

    # Futures
    gold_futures.history().to_csv('data/futures/gold.csv', index=False)

