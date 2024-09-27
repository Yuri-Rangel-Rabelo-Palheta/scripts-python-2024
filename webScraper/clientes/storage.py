import csv

def save_to_csv(data, filename):
    # Defina os nomes dos campos (colunas) para o arquivo completo
    fieldnames = ['name', 'email', 'phone']

    # Abra o arquivo para escrita dos dados completos
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados de cada cliente
        for cliente in data:
            writer.writerow(cliente)

    # Agora, para salvar os números de telefone em 'numeros.csv'
    with open('numeros.csv', mode='w', newline='', encoding='utf-8') as file:
        # O campo 'numero' será a única coluna no segundo arquivo
        writer = csv.writer(file)
        
        # Escreve o cabeçalho para o arquivo de números de telefone
        writer.writerow(['numero'])
        
        # Escreve os números de telefone únicos no arquivo 'numeros.csv'
        for cliente in data:
            # Extrai o número de telefone e escreve no arquivo
            phone = cliente.get('phone')
            if phone:
                writer.writerow([phone])




""" import csv

def save_to_csv(data, filename):
    # Defina os nomes dos campos (colunas) que o CSV terá
    fieldnames = ['name', 'email', 'phone']  # Adicione 'name' e 'phone'

    # Abra o arquivo para escrita
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados de cada cliente
        for cliente in data:
            writer.writerow(cliente)

    # Abra o arquivo para escrita
    with open('numeros.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames='numero')
        
        # Escreve o cabeçalho
        writer.writeheader()
        
        # Escreve os dados de cada cliente
        for cliente in data:
            writer.writerow(cliente.get('phone')) """
