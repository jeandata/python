import pandas as pd

df = pd.read_csv('./vendas.csv')
df_filtrado = df[df['entregue'] == True]

print(df_filtrado)