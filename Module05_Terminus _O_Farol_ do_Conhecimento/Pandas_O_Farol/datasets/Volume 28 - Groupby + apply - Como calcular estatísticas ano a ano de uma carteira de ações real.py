import pandas as pd
import numpy as np

# criar um intervalo de datas
date_range = pd.date_range(start='2019-01-01', end='2022-12-31', freq='D')

# criar uma lista de anos com base no índice
anos = [date.year for date in date_range]

# criar o DataFrame com valores fixos para a coluna "Valores"
df = pd.DataFrame({'Valores': [10]*len(date_range), 'Anos': anos}, index=date_range)

# mostrar o DataFrame

df.loc[(df["Anos"] == 2022),"Valores"] = 60

print(df)
