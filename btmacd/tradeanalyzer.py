from collections import OrderedDict

from backtrader.analyzers import TradeAnalyzer


class ResultAnalyzer(TradeAnalyzer):
    def get_analysis(self):
        analysis = OrderedDict()
        analysis["result"] = self.rets["pnl"]["net"]["total"]
        analysis["mean trade profit"] = self.rets["pnl"]["net"]["average"]
        analysis["count trades"] = self.rets["total"]["total"]
        analysis["count pos trades"] = self.rets["won"]["total"]
        analysis["count neg trades"] = self.rets["lost"]["total"]
        analysis["sum pos trades"] = self.rets["won"]["pnl"]["total"]
        analysis["sum neg trades"] = self.rets["lost"]["pnl"]["total"]
        analysis["relative pos trades"] = self.rets["won"]["total"] / self.rets["total"]["total"]
        analysis["relative neg trades"] = self.rets["lost"]["total"] / self.rets["total"]["total"]

        return analysis
