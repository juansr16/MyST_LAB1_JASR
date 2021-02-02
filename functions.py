import pandas as pd
import yfinance as yf
import data as dt

# Get tickers
tickers = dt.data['Ticker']
for i in range(0, len(tickers)):
    tickers[i] = tickers[i] + '.MX'

# Get weighing
weight = dt.data['Peso (%)']
for i in range(0, len(weight)):
    weight[i] = weight[i] / 100

# Union de tickers y pesos
w = pd.concat([tickers, weight], axis=1)

# Tickers malos y obtener su index para sumar su ponderacion
tm = ['KOFL.MX', ]
a = w[w['Ticker'] == tm[0]].index.values.astype(int)
t = a[0]
t = w.loc[t, :].tolist()
w.loc[len(w) - 1, 'Peso (%)'] = float(w.loc[len(w) - 1, 'Peso (%)']) + t[1]

# Limpiar datos
tickers = tickers.str.replace('*', '')
tickers = tickers.str.replace('LIVEPOLC.1.MX', 'LIVEPOLC-1.MX')
tickers = tickers.str.replace('MEXCHEM.MX', 'ORBIA.MX')
tickers = tickers.str.replace('GFREGIOO.MX', 'RA.MX')
tickers = tickers.str.replace('MXN.MX', 'CASH')
tickers = tickers.drop([10])
w = w.drop([10])

tickers = tickers.tolist()

# Get historical data
p = yf.download(tickers[0:len(tickers)], start="2018-01-31", end="2021-01-15")
p = p.dropna()