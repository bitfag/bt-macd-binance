#!/usr/bin/env python

import logging

import backtrader as bt

from btmacd.binance_feed import BinanceCSVData
from btmacd.macd_strategy import MacdStrategy
from btmacd.sizers import CustomAllInSizer
from btmacd.tradeanalyzer import ResultAnalyzer
from btmacd.tradeswriter import TradesWriter

log = logging.getLogger("btmacd")
log.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
handler.setFormatter(formatter)
log.addHandler(handler)


def runstrat():

    # cheat_on_open enabled to fix all-in mode
    cerebro = bt.Cerebro(cheat_on_open=True)
    cerebro.addstrategy(MacdStrategy)
    # Use full portfolio on each trade
    cerebro.addsizer(CustomAllInSizer)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio)
    cerebro.addanalyzer(ResultAnalyzer)
    cerebro.addanalyzer(TradesWriter, filename="mytrades.csv")

    datapath = "binance_ohlc.csv"
    # datapath = 'binance_ohlc_sample.csv'

    data = BinanceCSVData(dataname=datapath, reverse=False)

    cerebro.adddata(data)
    cerebro.broker.setcash(100.0)
    log.info("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    results = cerebro.run()
    log.info("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

    strat0 = results[0]
    for analyzer in strat0.analyzers:
        analyzer.print()

    cerebro.plot()


def main():
    runstrat()


if __name__ == "__main__":
    main()
