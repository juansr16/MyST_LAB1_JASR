import pandas as pd
import numpy as np
import yfinance as yf

# import data from csv file
data = pd.read_csv('C:/Users/JASR/Documents/Semestre Primavera 2021/Microestructura y Sistemas de '
                   'Trading/MyST_LAB1_JFME/files/naftrac_holdings_dec_2020/NAFTRAC_holdings/NAFTRAC_310118.csv',
                   skiprows=[0, 1])

# Get tickers
tickers = data['Ticker'].tolist()
for i in range(0, len(tickers)):
    tickers[i] = tickers[i]+'.MX'

# Get weighing
weight = data['Peso (%)'].tolist()
for i in range(0, len(weight)):
    weight[i] = weight[i] / 100

