import pandas as pd

pd.set_option('display.max_columns', 10)  # esta funcion nos ayuda a mostar todas las columnas
df_relative = pd.read_csv("../data/data_short.csv", index_col=0)  # relative path
# df_absolute = pd.read_csv("C:\\Users\\chiki\\Documents\\Clases\\Clases\\Metrologico\\data\\weather_data.csv") #absolute path
# imprmamos un resumen de los datos para ver como estan organizados
# print(df_relative.head(5))
# obtenemos el numero de columnas

# print(df_relative.count())
# print(df_relative.describe())
# obtenemos los header
headers = df_relative.columns
print(headers)
# seleccionaremos solo las columndas que tienen temperaturas
headers_filter = []
countrys = ["BE", "DE", "FR", "GB", "SE", "GR", "NL", "AT", "RO", "SK"]
for header in headers:
    country, type_data = header.split('_', 1)
    print(country, type_data)
    if type_data == "temperature" and country in countrys:
        headers_filter.append(header)

print(headers_filter)

# TODO Ejercicio ahora que filtre si se encuenta en estos 10 paises

df_filter_columns = df_relative[headers_filter]

"""Para filtrar por fecha si es el idex se puede hacer de la siguiente manera"""
df_filter_columns_rows = df_filter_columns.loc['1980-01-01':'1980-01-02']

"""Si no fuera el indice"""
# df[(df['date'] > '2013-01-01') & (df['date'] < '2013-02-01')]

# TODO Realizar el codigo para que el sistema le solicite dos fechas al usuario
# TODO Relizar la validacion para que las fechas esten correctas


# TODO Crear el nuevo dataframe, imprimir el head de 5 numeros y imprimir el resumen

df_filter_columns_rows.to_csv("../data/data_short_filter.csv")
