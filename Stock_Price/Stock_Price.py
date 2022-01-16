import yfinance as yf
import streamlit as sl
import pandas as pd

#%%
sl.write('''
         # Simple Stock Price App
         Shown are the stock **closing price** and ***volume*** of Google!
''')

ticker_symbol = 'GOOGL'
ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')
# Open    High    Low Close    Volume    Dividends    Stock Splits


#%%
sl.write('''
         ## Closing Price
''')
sl.line_chart(ticker_df.Close)
sl.write('''
         ## Volume Price
''')
sl.line_chart(ticker_df.Volume)

#%%