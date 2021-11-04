import numpy as np
import pandas as pd

df_relative = pd.read_csv("../data/data_short_filter.csv", index_col=0)  # relative path
data_matriz = df_relative.values
headers = df_relative.columns
dates = df_relative.index

# TODO obtener el maximo de cada columna

# TODO obtener el minimo de cada columna

# TODO obtener el promedio de cada columna

# TODO obtener la desviacion estandar de cada columna
