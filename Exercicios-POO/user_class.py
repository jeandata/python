from src.interface.utils.csv_class import CsvProcessor

arquivo_csv = './vendas.csv'
filtro = 'entregue'
tipo = True
filtro2 = 'price'
valor = 200

arquivo = CsvProcessor(arquivo_csv)
arquivo.carregar_csv()
df_final = arquivo.filtrar_por([filtro, filtro2], [tipo, valor])
print(df_final)