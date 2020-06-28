import csv

from backtrader import Analyzer, Order


class TradesWriter(Analyzer):
    params = (("filename", "trades.csv"),)

    def start(self):
        self.operations = []

    def notify_order(self, order):
        if order.status != Order.Completed:
            return

        operation = {"type": "buy" if order.isbuy() else "sell", "price": order.executed.price}
        self.operations.append(operation)

    def stop(self):
        with open(self.p.filename, "w") as csvfile:
            fieldnames = self.operations[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames)
            for op in self.operations:
                writer.writerow(op)
