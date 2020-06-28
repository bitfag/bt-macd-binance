from datetime import datetime

from backtrader.feeds import GenericCSVData


def parse_milliseconds(timestamp):
    return datetime.fromtimestamp(int(timestamp) / 1000)


class BinanceCSVData(GenericCSVData):

    params = (
        ("dtformat", parse_milliseconds),
        ("datetime", 0),
        ("time", -1),
        ("high", 2),
        ("low", 3),
        ("open", 1),
        ("close", 4),
        ("volume", 5),
        ("openinterest", -1),
    )
