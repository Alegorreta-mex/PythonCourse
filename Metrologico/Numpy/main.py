import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

df_relative = pd.read_csv("../data/data_short_filter.csv", index_col=0)  # relative path
data_matriz = df_relative.values
headers = df_relative.columns
dates = df_relative.index
"""Seccion de Procesamiento"""
# TODO obtener el maximo de cada columna
maximos = data_matriz.max(axis=0)
# TODO obtener el minimo de cada columna
minimos = data_matriz.min(axis=0)
# TODO obtener el promedio de cada columna
mean = data_matriz.mean(axis=0)
# TODO obtener la desviacion estandar de cada columna
std = data_matriz.std(axis=0)
# TODO normalizar

"""Seccion de Graficacion"""
pdf = matplotlib.backends.backend_pdf.PdfPages("output.pdf")

for name, data, maximo, minimo, mean, std in zip(headers, data_matriz.T, maximos, minimos, mean, std):
    fig, axes = plt.subplots()
    fig.suptitle(name, fontsize=16)
    axes.plot(data)
    axes.axhline(maximo, linestyle="dashdot", color='r')
    axes.axhline(minimo, linestyle="dashdot", color='r')
    axes.axhline(mean, linestyle="dashed", color='g')
    axes.fill_between([x for x in range(0, len(data))], mean + std, mean - std, alpha=.2, color='y')
    axes.axhline(mean + std, linestyle="dotted", color='y')
    axes.axhline(mean - std, linestyle="dotted", color='y')
    pdf.savefig(fig)
pdf.close()
