import json
import os.path
import tempfile

import pytest

from btmacd.binance_fetcher import BinanceFetcher


def load_fixture(filename):
    with open(filename) as json_file:
        data = json.load(json_file)

    return data


@pytest.fixture()
def fetcher():
    _, filename = tempfile.mkstemp()
    fetcher = BinanceFetcher("BTCUSD", filename=filename)
    return fetcher


def test_fetch(fetcher, monkeypatch):
    def mock(*args):
        return load_fixture("tests/fixtures/ohlc_binance.json")

    monkeypatch.setattr(fetcher.client, "get_historical_klines_generator", mock)
    fetcher.fetch()

    assert os.path.getsize(fetcher.filename) > 0
