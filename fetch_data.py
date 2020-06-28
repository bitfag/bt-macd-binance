#!/usr/bin/env python

from btmacd.binance_fetcher import BinanceFetcher


def main():
    fetcher = BinanceFetcher("BTCUSDT", filename="binance_ohlc.csv", start_date="01.01.2018")
    fetcher.fetch()


if __name__ == "__main__":
    main()
