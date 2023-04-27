from webull import webull
import time
import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta as pta
from quoter.quoter import Quoter
from quoter.quoter_Webull import Quoter_Webull
from quoter.quoter_Yahoo import Quoter_Yahoo


class Strategy:
    def __init__(self):
        # define your own strategy name, and indicator
        self.strategy_name = ''
        self.indicator = ''

        # set market data quoter
        # default is yh_quoter, fast and stable
        self.yh_quoter = Quoter_Yahoo()
        self.wb_quoter = Quoter_Webull()

        # set portfolio:
        # create trading strategy initialization attributes
        self.init_asset = 1000000
        self.init_cash = 1000000
        self.init_stock = ''
        self.init_portfolio = {'cash': self.init_cash, 'stock': self.init_stock, 'asset': self.init_asset}

        # set oder history
        self.order_history = []
        # self.order_history = pd.DataFrame(columns=['datetime', 'order_id', 'action', 'order_type',
        #                                            'stock', 'price', 'order_quantity', 'amount', 'status'])
        # self.order_history.set_index('datetime', inplace=True)

        # create trading strategy attributes
        self.cash = self.init_cash
        self.stock = self.init_stock
        self.asset = self.init_asset
        self.portfolio = {'cash': self.cash, 'stock': self.stock, 'asset': self.asset}

        # create trading strategy parameters
        self.buy = False
        self.sell = False
        self.hold = False
        self.buy_price = 0
        self.sell_price = 0
        self.hold_price = 0

        # create trading strategy indicators, default is 0, you can define your own indicators
        self.ema = 0
        self.sma = 0
        self.adx = 0
        self.obv = 0
        self.bbands = 0
        self.aroon = 0
        self.atr = 0
        self.cci = 0
        self.cmo = 0
        self.coppock = 0
        self.dpo = 0
        self.dmi = 0
        self.ichimoku = 0
        self.kst = 0
        self.macd = 0
        self.mfi = 0
        self.mom = 0
        self.pivots = 0
        self.ppo = 0
        self.psl = 0
        self.roc = 0
        self.rsi = 0
        self.rvi = 0
        self.stoch = 0
        self.tsi = 0
        self.uo = 0
        self.willr = 0
        self.vwap = 0
        self.vwma = 0
        self.vwmacd = 0
        self.zlema = 0


    """
    Response time: 
        wb_quoter:  around 300 - 800 ms
        yh_quoter:  around 200 - 400 ms
        
    Intraday:
    < 15 min:   yh_quoter will get more data
    > 15 min:   Quoter_Webull will get more data
    = 1h:       yh_quoter will get more data
    
    >= 1d:      yh_quoter will get more data
    """
    def strategy_decision(self, stock):
        """
        Example strategy, based on RSI, from Webull and chatGPT.
        Buy when RSI < 30 and Sell when RSI > 70.
        Only for reference, please build your own strategy based on this file
        :return:
        """
        # get stock data
        stock_data = self.yh_quoter.get_1min_bar(stock=stock, count=100)
        # stock_data = self.wb_quoter.get_1min_bar(stock=stock, count=100)

        # calculate RSI
        self.rsi = pta.rsi(stock_data['close'], length=14)

        # make decision
        if stock_data['rsi'].iloc[-1] < 30:
            # buy
            pass
        elif stock_data['rsi'].iloc[-1] > 70:
            # sell
            pass
        else:
            # hold
            pass
        pass

    def strategy_rules(self):
        pass

    def make_decision_1m(self):
        pass

    def make_decision_5m(self):
        pass

    def make_decision_15m(self):
        pass

    def make_decision_1h(self):
        pass

    def make_decision_1d(self):
        pass

    def check_1m_bar(self):
        pass

    def check_2m_bar(self):
        pass

    def check_5m_bar(self):
        pass

    def check_15m_bar(self):
        pass

    def check_30m_bar(self):
        pass

    def check_1h_bar(self):
        pass

    def check_1d_bar(self):
        pass

    def check_1w_bar(self):
        pass

