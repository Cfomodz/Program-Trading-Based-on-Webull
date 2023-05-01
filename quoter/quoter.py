from webull import webull
import datetime
import time
import pandas as pd
import yfinance as yf
from utils.util import *


class Quoter:
    def __init__(self):
        self.name = "Quoter"
        self.quoter_wb = webull()

    """

        Yahoo:
            Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo; (Intraday data cannot extend last 60 days)
            Valid count/period:
                1m:             5d
                2m,5m,15m,30m:  1mo
                1h:             2y
                d1 and above:   10y
            
            Set as default quoter in strategy, fast and stable.
            
            
        Webull:
            Valid intervals: m1, m5, m15, m30, d1;  (h1, h2, h4, w1 are currently not working)
            Valid count/period:
                m1:     1200
                m5:     1200
                m15:    1200
                m30:    1049
                d1:     1200
            interval : str
            
            Set as default quoter in trade/order related, real time ask and bid price.
    """

    def get_current_quote(self, stock):
        pass

    def get_1min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_3min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_5min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_15min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_30min_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_2h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_4h_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1d_bar(self, stock, count='max', extend_trading=False):
        pass

    def get_1w_bar(self, stock, count='max', extend_trading=False):
        pass
