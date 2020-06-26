import csv

from binance.client import Client


class BinanceFetcher:
    def __init__(self, symbol, filename="binance_ohlc.csv", start_date="01.01.2018"):
        self.symbol = symbol
        self.filename = filename
        self.start_date = start_date
        self.client = Client()

    def fetch(self):

        with open(self.filename, "w") as csvfile:
            writer = csv.writer(csvfile)
            klines = self.client.get_historical_klines_generator(
                self.symbol, Client.KLINE_INTERVAL_1HOUR, self.start_date
            )
            for entry in klines:
                writer.writerow(entry)
