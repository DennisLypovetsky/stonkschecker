import yfinance as yf

myTicker = yf.Ticker("BTC-USD")

# get historical market data
hist = myTicker.history(period="5d")
print(hist)
