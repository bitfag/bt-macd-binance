#!/usr/bin/env python

from btmacd.binance_fetcher import BinanceFetcher


def main():
    fetcher = BinanceFetcher("BTCUSDT")
    fetcher.fetch()


if __name__ == "__main__":
    main()
