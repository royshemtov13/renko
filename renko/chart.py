from typing import Optional

import pandas as pd

from renko.bar import RenkoBar


class RenkoChart:
    def __init__(self, symbol: str, brick_size: float):
        self.symbol = symbol
        self.brick_size = brick_size
        self._bars: list[RenkoBar] = []

    def __len__(self) -> int:
        return len(self._bars)

    def bars(self, length: Optional[int] = None) -> list[RenkoBar]:
        if length:
            return self._bars[-length:]
        return self._bars

    def data(self, length: Optional[int] = None) -> pd.DataFrame:
        if length:
            bars = [bar.dict() for bar in self._bars[-length:]]
        else:
            bars = [bar.dict() for bar in self._bars]
        columns = list(RenkoBar.__fields__.keys())
        data = pd.DataFrame(bars, columns=columns)
        return data

    def add(self, timestamp: float, close: float) -> int:
        if not self._bars:
            bar = RenkoBar(
                timestamp=timestamp,
                open=close,
                high=close,
                low=close,
                close=close,
                trend=0,
            )
            self._bars.append(bar)
            return 0

        before = len(self)

        last_brick = self._bars[-1]
        if close >= last_brick.high:
            self._next(timestamp, close)
        elif close <= last_brick.low:
            self._next(timestamp, close)
        else:
            return 0

        after = len(self)
        new_bars = after - before
        return new_bars

    def _next(self, timestamp: float, close: float) -> None:
        while True:
            last_bar = self._bars[-1]

            if last_bar.trend == 1:
                brick_upper_limit = last_bar.close + self.brick_size
                brick_lower_limit = last_bar.close - (2 * self.brick_size)
            elif last_bar.trend == -1:
                brick_lower_limit = last_bar.close - self.brick_size
                brick_upper_limit = last_bar.close + (2 * self.brick_size)
            else:
                brick_upper_limit = last_bar.close + self.brick_size
                brick_lower_limit = last_bar.close - self.brick_size

            if close >= brick_upper_limit:
                multiplier = 2 if last_bar.trend == -1 else 1
                new_trend = 1
                open_ = last_bar.close if new_trend == last_bar.trend else last_bar.open
                new_close = last_bar.close + (multiplier * self.brick_size)
                high = new_close
                low = open_
            elif close <= brick_lower_limit:
                multiplier = 2 if last_bar.trend == 1 else 1
                new_trend = -1
                open_ = last_bar.close if new_trend == last_bar.trend else last_bar.open
                new_close = last_bar.close - (multiplier * self.brick_size)
                low = new_close
                high = open_
            else:
                break

            new_bar = RenkoBar(
                timestamp=timestamp,
                open=open_,
                high=high,
                low=low,
                close=new_close,
                trend=new_trend,
            )
            self._bars.append(new_bar)
