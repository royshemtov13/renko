import random

import pandas as pd

from renko.chart import RenkoChart


def generate_date_range(length: int) -> pd.DatetimeIndex:
    start = pd.Timestamp.now() - pd.Timedelta(minutes=length)
    index = pd.date_range(start=start, periods=length, freq="1min")
    return index


def random_data(mean: int, std: int, length: int) -> list[float]:
    prices = [mean]
    for _ in range(1, length):
        price = random.gauss(prices[-1], std)
        prices.append(price)
    return prices


def random_ohlc(length: int, starting: float, std: int) -> pd.DataFrame:
    data = {
        "open": random_data(starting, std, length),
        "high": random_data(starting, std, length),
        "low": random_data(starting, std, length),
        "close": random_data(starting, std, length),
        "volume": random_data(1000, 200, length),
    }
    index = generate_date_range(length)
    ohlc = pd.DataFrame(data, index=index)
    return ohlc


def random_renko_chart(
    length: int, start: int, std: int, brick_size: float
) -> pd.DataFrame:
    ohlc = random_ohlc(length, start, std)
    renko_chart = RenkoChart("TEST", brick_size)
    timestamps = [int(ts.timestamp()) for ts in ohlc.index.to_list()]
    prices = ohlc["close"].to_list()
    for ts, c in zip(timestamps, prices):
        renko_chart.add(ts, c)
    data = renko_chart.data()
    return data
