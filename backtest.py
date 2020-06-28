#!/usr/bin/env python

import logging

import backtrader as bt
import click

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


def runstrat(data_file="binance_ohlc.csv", trades_file="mytrades.csv", plot=False):

    # cheat_on_open enabled to fix all-in mode
    cerebro = bt.Cerebro(cheat_on_open=True)
    cerebro.addstrategy(MacdStrategy)

    # Use full portfolio on each trade
    cerebro.addsizer(CustomAllInSizer)
    cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.02)
    cerebro.addanalyzer(ResultAnalyzer)
    cerebro.addanalyzer(TradesWriter, filename=trades_file)

    data = BinanceCSVData(dataname=data_file, reverse=False)
    cerebro.adddata(data)

    cerebro.broker.setcash(100.0)

    log.info("Starting Portfolio Value: %.2f" % cerebro.broker.getvalue())
    results = cerebro.run()
    log.info("Final Portfolio Value: %.2f" % cerebro.broker.getvalue())

    strat0 = results[0]
    for analyzer in strat0.analyzers:
        analyzer.print()

    if plot:
        cerebro.plot()


@click.command()
@click.option("--plot", is_flag=True, default=False, help="Plot chart")
@click.argument("filename")
def main(plot, filename):
    """Run backtets on FILENAME, which must be a csv file."""
    runstrat(data_file=filename, plot=plot)


if __name__ == "__main__":
    main()
