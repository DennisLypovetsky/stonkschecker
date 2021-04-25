import yfinance as yf
import pandas as pd

btc = yf.Ticker("BTC-USD")

btcHist = btc.history(start="2020-03-01")
btcHistToList = pd.DataFrame(btcHist).values.tolist()

print(btcHist)
print("--------------------")
print(btcHistToList[1][0])
print("--------------------")
print(btcHistToList[-1][0])

# print(btcHist)
# print(btcHist[1])
# # print(btcHist[1, 1])



