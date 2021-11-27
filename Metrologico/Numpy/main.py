import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


df_relative = pd.read_csv("../data/data_short_filter.csv", index_col=0)  # relative path
data_matriz = df_relative.values
headers = df_relative.columns
dates = df_relative.index

# TODO obtener el maximo de cada columna
print(data_matriz.shape)
fig, axes = plt.subplots()  # Create a figure containing a single axes.
axes.plot(data_matriz)  # Plot some data on the axes.
plt.show()

# TODO obtener el minimo de cada columna

# TODO obtener el promedio de cada columna

# TODO obtener la desviacion estandar de cada columna

# TODO normalizar
