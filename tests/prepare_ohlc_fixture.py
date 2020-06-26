#!/usr/bin/env python

from binance.client import Client
import json
import os.path
import sys


def main():
    client = Client()
    klines = client.get_historical_klines('BTCUSDT', Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC", limit=3)
    filename = os.path.join(os.path.dirname(sys.argv[0]), 'fixtures', 'ohlc_binance.json')
    with open(filename, 'w') as f:
        json.dump(klines, f, indent=2)


if __name__ == '__main__':
    main()
