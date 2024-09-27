import pandas as pd
from datetime import datetime

# Carregar os dados extraídos de um arquivo CSV
input_file = 'clientes.csv'  # Substitua pelo caminho do seu arquivo
df = pd.read_csv(input_file)

# Remover linhas duplicadas com base nas colunas 'email' e 'phone'
df_cleaned = df.drop_duplicates(subset=['email','phone'])

# Gerar um novo nome de arquivo com a data e hora atual
current_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
output_file = f'arquivo_limpo_{current_time}.csv'

# Salvar os dados limpos no novo arquivo CSV
df_cleaned.to_csv(output_file, index=False)

print(f'Arquivo {input_file} limpo e salvo como {output_file}')
