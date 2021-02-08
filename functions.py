import pandas as pd
import yfinance as yf
import math
import numpy as np

from data import data, dates


# Get tickers
def Tickers(data):
    tickers = data['Ticker']
    tickers = tickers + '.MX'
    return tickers


tickers = Tickers(data)


# Get weighing
def Weight(data):
    weight = data['Peso (%)']
    weight = weight / 100
    return weight


weight = Weight(data)

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
tickers = tickers.str.replace('MXN.MX', 'cash')
tickers = tickers.drop([10])
w = w.drop([10])
w['Ticker'] = tickers
w = w.sort_values(by='Ticker')
w = w.reset_index()

# Convertir Tickers  Lista para descargar datos historicos
tickers = tickers.tolist()


# Obtener datos historicos y quedarse con los precios de cierre
def Get_price(tickers):
    p = yf.download(tickers[0:len(tickers) - 1], start="2018-01-30", end="2021-01-15")
    p = p.dropna()
    # Obtener los precios de cierre
    closes = p['Close']
    return closes


closes = Get_price(tickers)

# Precios de fechas deseadas
precios = closes.loc[dates[0:len(dates)]]
precios = precios.sort_values(by='Date')

# Formulacion del problema
# Monto a invertir
i = 1000000
# Comision
c = 0.00125


# Funcion para obtener portafolio de accion
def Port(amount: float):
    weights = w['Peso (%)']
    precio = closes.iloc[0, :]
    montos = (amount * weights)
    for i in range(0, len(precio)):
        weight.iloc[i] = math.floor(montos.iloc[i] / precio.iloc[i])
    port = pd.concat([w['Ticker'], weight], axis=1)
    port = port.drop([34, 35])
    return port


# Funcion para calcular el total del portafolio inicial
def Port_in(port):
    na = port['Peso (%)']
    precio = closes.iloc[0, :]
    precio = precio.reset_index()
    precio = precio.iloc[:, 1]
    port_m = na * precio
    s = port_m.sum()
    return s


# Funcion para obtener cash
def Cash(amount: float, vi: float, com: float):
    cash = w.iloc[len(w) - 1, 2]
    cash = (amount - vi)
    return cash


# Funcion para obtener el capital
def Capital(precios, port, cash, vi):
    capital = []
    for i in range(0, len(precios)):
        a = (((precios.iloc[i, :] * port.iloc[:, 1].tolist()).sum()) + cash) - (vi * c)
        capital.append(a)
    capital = pd.DataFrame(capital, columns=["Capital"])
    capital.loc[0] = capital.loc[0] + (vi * c)
    return capital


# Funcion para obtener el rendimiento
def Rendimiento(cap):
    rend = cap.pct_change()
    rend = rend.fillna(0)
    return rend


# Funcion para obtener el rendimiento acumulado
def Rend_acum(rend):
    rend = np.cumsum(rend)
    return rend


# Funcion para generar el resumen de la inversion Pasiva
# Feachas, Capital, Rendimiento y Rendimeinto acumulado
def df_pasiva(precios, capital, rendimiento, rend_a):
    df_pasiva = pd.DataFrame()
    df_pasiva['Timestamp'] = precios.index
    df_pasiva['Capital'] = capital
    df_pasiva['Rendimiento'] = rendimiento
    df_pasiva['Rendimiento acumulado'] = rend_a
    return df_pasiva
