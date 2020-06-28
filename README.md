# bt-macd-binance

This repo is an algotrading test task. The goal is to backtest simple MACD-based startegy on historical data of Binance
BTC/USD pair.

## Setup

1. Install [poetry](https://python-poetry.org/docs/)
2. Run `poetry install` to install the dependencies
3. Activate the environment using `poettry shell`

## Running

Obtain historical data feed:

```
./fetch_data.py
```

Run the backtest:

```
./backtest.py binance_ohlc.csv
```

Optionally enable chart plotting: `./backtest.py --plot ...`
