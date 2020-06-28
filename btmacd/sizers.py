from backtrader.sizers import PercentSizer


class CustomAllInSizer(PercentSizer):
    params = (("percents", 99.5),)
