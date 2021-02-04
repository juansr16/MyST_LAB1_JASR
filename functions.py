import pandas as pd
import yfinance as yf
from data import data

# Get tickers
tickers = data['Ticker']
tickers = tickers + '.MX'

# Get weighing
weight = data['Peso (%)']
weight = weight / 100

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
w['Ticker'] = tickers

tickers = tickers.tolist()

# Obtener datos historicos
p = yf.download(tickers[0:len(tickers)], start="2018-01-31", end="2021-01-15")
p = p.dropna()

# Obtener los precios de cierre
closes = p['Close']


# Funcion para obtener portafolio de accion
def port(amount:float):
    weights = w['Peso (%)']
    precio = closes.iloc[0, :]
    montos = (amount * weights)
    for i in range(0, len(precio)):
        weight.iloc[i] = round(montos.iloc[i] / precio.iloc[i])
    get_port = pd.concat([w['Ticker'], weight], axis=1)
    return get_port
