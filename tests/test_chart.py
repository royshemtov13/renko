import pytest

from renko.bar import RenkoBar
from renko.chart import RenkoChart


@pytest.fixture
def chart():
    return RenkoChart("TEST", 1)


def test_chart_length(chart):
    assert len(chart) == 0
    chart.add(1, 100)
    assert len(chart) == 1
    chart.add(2, 101)
    assert len(chart) == 2


def test_add_one_bar(chart):
    assert len(chart) == 0
    chart.add(1, 100)
    assert len(chart) == 1
    assert chart._bars[0].timestamp == 1
    assert chart._bars[0].open == 100
    assert chart._bars[0].high == 100
    assert chart._bars[0].low == 100
    assert chart._bars[0].close == 100
    assert chart._bars[0].trend == 0


def test_add_bulk_up(chart):
    assert len(chart) == 0
    for ts, c in zip([1, 2, 3], [100, 101, 102]):
        chart.add(ts, c)
    assert len(chart) == 3
    assert chart._bars[0].timestamp == 1
    assert chart._bars[0].open == 100
    assert chart._bars[0].high == 100
    assert chart._bars[0].low == 100
    assert chart._bars[0].close == 100
    assert chart._bars[0].trend == 0
    assert chart._bars[1].timestamp == 2
    assert chart._bars[1].open == 100
    assert chart._bars[1].high == 101
    assert chart._bars[1].low == 100
    assert chart._bars[1].close == 101
    assert chart._bars[1].trend == 1
    assert chart._bars[2].timestamp == 3
    assert chart._bars[2].open == 101
    assert chart._bars[2].high == 102
    assert chart._bars[2].low == 101
    assert chart._bars[2].close == 102
    assert chart._bars[2].trend == 1


def test_add_bulk_down(chart):
    assert len(chart) == 0
    for ts, c in zip([1, 2, 3], [100, 99, 98]):
        chart.add(ts, c)
    assert len(chart) == 3
    assert chart._bars[0].timestamp == 1
    assert chart._bars[0].open == 100
    assert chart._bars[0].high == 100
    assert chart._bars[0].low == 100
    assert chart._bars[0].close == 100
    assert chart._bars[0].trend == 0
    assert chart._bars[1].timestamp == 2
    assert chart._bars[1].open == 100
    assert chart._bars[1].high == 100
    assert chart._bars[1].low == 99
    assert chart._bars[1].close == 99
    assert chart._bars[1].trend == -1
    assert chart._bars[2].timestamp == 3
    assert chart._bars[2].open == 99
    assert chart._bars[2].high == 99
    assert chart._bars[2].low == 98
    assert chart._bars[2].close == 98
    assert chart._bars[2].trend == -1


def test_add_bulk_up_and_down(chart):
    assert len(chart) == 0
    for ts, c in zip([1, 2, 3, 4, 5], [100, 101, 99, 101, 99]):
        chart.add(ts, c)
    assert len(chart) == 5
    assert chart._bars[0].timestamp == 1
    assert chart._bars[0].open == 100
    assert chart._bars[0].high == 100
    assert chart._bars[0].low == 100
    assert chart._bars[0].close == 100
    assert chart._bars[0].trend == 0
    assert chart._bars[1].timestamp == 2
    assert chart._bars[1].open == 100
    assert chart._bars[1].high == 101
    assert chart._bars[1].low == 100
    assert chart._bars[1].close == 101
    assert chart._bars[1].trend == 1
    assert chart._bars[2].timestamp == 3
    assert chart._bars[2].open == 100
    assert chart._bars[2].high == 100
    assert chart._bars[2].low == 99
    assert chart._bars[2].close == 99
    assert chart._bars[2].trend == -1
    assert chart._bars[3].timestamp == 4
    assert chart._bars[3].open == 100
    assert chart._bars[3].high == 101
    assert chart._bars[3].low == 100
    assert chart._bars[3].close == 101
    assert chart._bars[3].trend == 1
    assert chart._bars[4].timestamp == 5
    assert chart._bars[4].open == 100
    assert chart._bars[4].high == 100
    assert chart._bars[4].low == 99
    assert chart._bars[4].close == 99
    assert chart._bars[4].trend == -1


def test_next(chart):
    chart._bars = [
        RenkoBar(timestamp=0, open=100, high=101, low=100, close=101, trend=1)
    ]
    assert len(chart) == 1
    ts = 1
    close = 102
    chart._next(ts, close)
    assert chart._bars[-1].open == 101
    assert chart._bars[-1].high == 102
    assert chart._bars[-1].low == 101
    assert chart._bars[-1].close == 102
    assert chart._bars[-1].trend == 1

    assert len(chart) == 2
