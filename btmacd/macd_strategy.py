import logging

import backtrader as bt

log = logging.getLogger(__name__)


class MacdStrategy(bt.Strategy):
    def __init__(self):
        self.macd = bt.indicators.MACD(period_me1=12, period_me2=26, period_signal=9)
        self.signal_over_macd = self.macd.lines.signal > self.macd.lines.macd

    def log(self, txt, dt=None):
        """Adds date of current historical data being processed."""
        dt = dt or self.datas[0].datetime.date(0)
        log.info("%s, %s" % (dt.isoformat(), txt))

    def next(self):

        if not self.position:
            # TODO: refactor to bt.indicators.CrossOver
            if self.macd.lines.macd[0] > 0:
                # Signal crosses the MACD line from down to up
                if self.signal_over_macd[0] and not self.signal_over_macd[-1]:
                    self.log("BUY CREATE, %.2f" % self.data.close[0])
                    self.order = self.buy()
        elif self.macd.lines.macd[0] < 0:
            # Signal crosses the MACD line from up to down
            if not self.signal_over_macd[0] and self.signal_over_macd[-1]:
                self.log("SELL CREATE, %.2f" % self.data.close[0])
                self.order = self.close()

    def notify_order(self, order):
        if order.status in [order.Submitted, order.Accepted]:
            # Buy/Sell order submitted/accepted to/by broker - Nothing to do
            return

        # Check if an order has been completed
        # Attention: broker could reject order if not enough cash
        if order.status in [order.Completed]:
            if order.isbuy():
                self.log("BUY EXECUTED, %.2f" % order.executed.price)
            elif order.issell():
                self.log("SELL EXECUTED, %.2f" % order.executed.price)

        elif order.status in [order.Canceled, order.Margin, order.Rejected]:
            self.log("Order Canceled/Margin/Rejected: {}".format(order.status))

        # Write down: no pending order
        self.order = None
