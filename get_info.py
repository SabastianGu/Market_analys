import re
import requests

coin_list = (
    "BTC", "ETH", "LTC", "NEO", "BNB", "XRP", "LINK", "EOS", "TRX",
    "ETC", "XLM", "ZEC", "ADA", "QTUM", "DASH", "XMR", "BTT"
)

binance_DS = open ('multicoin_dataset.csv', "wb")
binance_DS.write(bytes("unix,date,symbol,open,high,low,close,Volume BTC,Volume USDT,tradecount", 'utf-8'))

for coin in coin_list:
    request_str = f"http://www.cryptodatadownload.com/cdd/Binance_{coin}USDT_minute.csv"
    r = requests.get(request_str)
    coin_csv = r.content
    binance_DS.write(coin_csv)

binance_DS.close()



#data_history

gemini_DS = open ('gemini_history.csv', "wb")
gemini_DS.write(bytes("Unix Timestamp,Date,Symbol,Open,High,Low,Close,Volume", 'utf-8'))

#BTC
for year in range (2015, 2021):
    request_str = f"http://www.cryptodatadownload.com/cdd/gemini_BTCUSD_{year}_1min.csv"
    r = requests.get(request_str)
    coin_csv = r.content
    gemini_DS.write(coin_csv)

# ETH
for year in range (2016, 2021):
    request_str = f"http://www.cryptodatadownload.com/cdd/gemini_ETHUSD_{year}_1min.csv"
    r = requests.get(request_str)
    coin_csv = r.content
    gemini_DS.write (coin_csv)


# LTC & ZEC

for year in range (2018, 2021):
    request_str = f"http://www.cryptodatadownload.com/cdd/gemini_LTCUSD_{year}_1min.csv"
    r = requests.get(request_str)
    coin_csv = r.content
    gemini_DS.write(coin_csv)

for year in range (2018, 2021):
    request_str = f"http://www.cryptodatadownload.com/cdd/gemini_ZECUSD_{year}_1min.csv"
    coin_csv = r.content
    gemini_DS.write(coin_csv)

gemini_DS.close()

