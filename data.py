from os import path, listdir
from os.path import isfile, join

import pandas as pd

# Obtener fechas y agregar fecha inicial
abspath = path.abspath('C:/Users/JASR/Documents/Semestre Primavera 2021/Microestructura y Sistemas de '
                       'Trading/MyST_LAB1_JFME/files/naftrac_holdings_dec_2020/NAFTRAC_holdings/')
dates = [f[8:-4] for f in listdir(abspath) if isfile(join(abspath, f))]
# Fecha anterior a la inversion
dates.append('300118')

# Obtener datos
data = pd.read_csv(abspath + '/NAFTRAC_310118.csv', skiprows=[0, 1])
data = data.dropna()
