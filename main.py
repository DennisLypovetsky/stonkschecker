import yfinance as yf
import pandas as pd

uah_usd = yf.Ticker("UAH=X")     # UAH/USD
btc_usd = yf.Ticker("BTC-USD")   # BTC/USD


def hist(pair=uah_usd, date="2019-04-01"):
    return pd.DataFrame(pair.history(start=date)).values.tolist()


date = "2020-04-01"
pair = btc_usd  # uah_usd | btc_usd

if pair == uah_usd:
    user_pair = "UAH"
    target_pair = "USD"

if pair == btc_usd:
    user_pair = "USD"
    target_pair = "BTC"


start_amount = 1000  # UAH | USD

gain = hist(pair, date)[-1][0] / hist(pair, date)[1][0] * 100 - 100
end_amount = start_amount * gain / 100


print(f"В {date} вы вложили свои {start_amount:,} {user_pair} в {target_pair}")
print(f"Тогда это стоило: {round(hist(pair, date)[1][0], 2):,}₴")
print(f"Cейчас это стоит: {round(hist(pair, date)[-1][0], 2):,}₴")
print("___")
print(f"Вложения в {target_pair} изменились на {round(gain, 2)}%")
print(f"Или на {round(end_amount, 0):,} UAH")
