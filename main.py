"""# -- --------------------------------------------------------------------------------------------------- -- # # --
project: Project made to show the profit of making a pasive investment.
        -- # # -- script: main.py : python script with the main functionality
        -- # # -- author: juansr16                                                                      -- # # --
        license: GPL-3.0 License                                                                            -- # # --
        repository: https://github.com/juansr16/MyST_LAB1_JFME
                    -- # # --
                    --------------------------------------------------------------------------------------------------- -- # """

import data as dt
import functions as fn

# Definir datos del problema
# Monto a invertir
i = 1000000
# Comision
c = 0.00125

# Obtener tickers
tickers = fn.Tickers(dt.data)

# Obtener pesos para el portafolio
weight = fn.Weight(dt.data)

# Despues de limpiar los datos descargar los precios
precios = fn.Get_price(fn.tickers)

# Funcion para generar el portafolio
port = fn.Port(i)

# Funcion para generar el valor total inicial del portafolio
vi = fn.Port_in(port)

# Funcion para obtener el cash de la operacion
cash = fn.Cash(i, vi, c)

# Funcion para obtener el Dataframe del capital de la operacion
capital = fn.Capital(fn.precios, port, cash, vi)

# Funcion para obtener los rendimientos de la transaccion
rend = fn.Rendimiento(capital)

# Funcion para obtener el rendimiento acumulado
ra = fn.Rend_acum(rend)

# Dataframe con los resultados de la operacion
df_p = fn.df_pasiva(fn.precios, capital, rend, ra)
print(df_p)
