import pandas as pd


from os import path

# Set path
abspath = path.abspath('C:/Users/JASR/Documents/Semestre Primavera 2021/Microestructura y Sistemas de '
                       'Trading/MyST_LAB1_JFME/files/naftrac_holdings_dec_2020/NAFTRAC_holdings/')
# Get data
data = pd.read_csv(abspath + '/NAFTRAC_310118.csv', skiprows=[0, 1])
data = data.dropna()
