# renko

renko. A renko trading library that can seamlessly perform real time calculations of price data with an open data stream to a live renko chart. enabling you to listen to live quotes and instantly update the renko chart.
By processing incoming quotes, the library continuously maintains an up-to-date renko chart that accurately reflects market activity. This real-time functionality empowers traders, analysts, and developers to make informed decisions and implement timely trading strategies based on the latest data.
And also this library has lots of features for deep analysis of renko chart activity. By taking any stock's OHLC data in past or a totally random data to create the renko chart it would represent to get insights on strategies.

## resources

- Poetry, a dependency managment tool: <https://python-poetry.org/docs/>
- Pandas, a data science library: <https://python-pandas>

## Features

- Generation of Renko charts from OHLC data
- Customizable brick sizes and chart configurations
- Backtesting and strategy evaluation capabilities
- Indicator calculation on Renko charts
- Live renko bars calculation with RabbitMQ
- Async support

## Installation

To use the Renko Trading Library, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/royshemtov13/renko.git
   ```

2. Install and load the required dependencies via poetry:

    ```shell
    poetry install
    ```

    Once installed you can load the environment by doing the following:

    ```shell
    poetry shell
    ```

3. That's it. Now we can use the RenkoChart Class

    ```python
    # import the RenkoChart class
    from renko.chart import RenkoChart

    # initializing with the symbol and the desired brick size
    renko_chart = RenkoChart(symbol="AAPL", brick_size=1.0)
    
    # using the built in random functions to generate a renko random renko chart
    renkos = random_renko_chart(
        length=1000,     # length of desired chart
        start=1000,      # starting price
        std=5,           # random standard deviation movement
        brick_size=5.0,  # brick size
    )

    # (e.g. renko chart table)
    | timestamp | open  | high  | low   | close | trend |
    |-----------|-------|-------|-------|-------|
    | 0         | 1000.0| 1000.0| 1000.0| 1000.0| 0     |
    | 1         | 1000.0| 1001.0| 1000.0| 1001.0| 1     |
    | 2         | 1000.0| 1000.0| 999.0 | 999.0 | -1    |
    | 3         | 999.0 | 999.0 | 998.0 | 998.0 | -1    |
    | 4         | 998.0 | 998.0 | 997.0 | 997.0 | -1    |
    | 5         | 997.0 | 997.0 | 996.0 | 996.0 | -1    |

    
    ```

# Contributing

Contributions to the Renko Trading Library are welcome! If you have any bug reports, feature requests, or improvements, please open an issue or submit a pull request. Please ensure that your code adheres to the existing code style and passes the tests.

License
This project is licensed under the MIT License.
