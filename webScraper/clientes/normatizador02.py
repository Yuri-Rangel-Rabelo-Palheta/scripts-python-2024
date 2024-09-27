import csv

def extract_and_save_numbers(input_file, output_file):
    numbers = set()  # Usando um set para evitar números duplicados

    # Leia o arquivo CSV de entrada
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            phone_number = row.get('phone')  # Substitua 'phone' pelo nome correto da coluna se necessário
            if phone_number:
                numbers.add(phone_number.strip())

    # Salve os números no arquivo 'numero.csv'
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['numero'])  # Escreve o cabeçalho

        for number in sorted(numbers):
            writer.writerow([number])

# Exemplo de uso:
input_file = 'clientes.csv'  # Substitua pelo nome do seu arquivo de entrada
output_file = 'numero.csv'
extract_and_save_numbers(input_file, output_file)


""" import csv
import re

def normalize_phone_number(phone_number):
    # Remove todos os caracteres não numéricos
    digits = re.sub(r'\D', '', phone_number)
    
    # Verifica se o número possui 11 dígitos (incluindo o 9 inicial)
    if len(digits) == 11 and digits[0] == '9':
        return digits  # Número já está no formato desejado
    
    # Verifica se o número possui 10 dígitos (sem o 9 inicial)
    if len(digits) == 10:
        return '9' + digits  # Adiciona o 9 inicial
    
    return None  # Retorna None se o número não for válido

def extract_and_save_numbers(input_file, output_file):
    numbers = set()  # Usando um set para evitar números duplicados

    # Leia o arquivo CSV de entrada
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            phone_number = row.get('phone')  # Substitua 'phone' pelo nome correto da coluna se necessário
            if phone_number:
                normalized_number = normalize_phone_number(phone_number.strip())
                if normalized_number:
                    numbers.add(normalized_number)

    # Salve os números normalizados no arquivo 'numero.csv'
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['numero'])  # Escreve o cabeçalho

        for number in sorted(numbers):
            writer.writerow([number])

# Exemplo de uso:
input_file = 'clientes.csv'  # Substitua pelo nome do seu arquivo de entrada
output_file = 'numero.csv'
extract_and_save_numbers(input_file, output_file)
 """


""" import csv

def extract_and_save_numbers(input_file, output_file):
    numbers = set()  # Usando um set para evitar números duplicados

    # Leia o arquivo CSV de entrada
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            phone_number = row.get('phone')  # Substitua 'phone' pelo nome correto da coluna se necessário
            if phone_number:
                numbers.add(phone_number.strip())

    # Salve os números no arquivo 'numero.csv'
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['numero'])  # Escreve o cabeçalho

        for number in sorted(numbers):
            writer.writerow([number])

# Exemplo de uso:
input_file = 'clientes.csv'  # Substitua pelo nome do seu arquivo de entrada
output_file = 'numero.csv'
extract_and_save_numbers(input_file, output_file)
 """
""" import csv
import re

def normalize_phone_number(phone):
    # Remove tudo que não é dígito
    phone = re.sub(r'\D', '', phone)
    
    # Considera somente números de celular (exemplo para o Brasil)
    # Números de celular têm 11 dígitos e começam com 9 (padrão Brasil)
    if len(phone) == 11 and phone.startswith('9'):
        return phone
    
    return None

def extract_unique_mobile_numbers(input_csv, output_csv):
    unique_numbers = set()

    with open(input_csv, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            phone = row['phone']
            normalized_phone = normalize_phone_number(phone)
            if normalized_phone:
                unique_numbers.add(normalized_phone)

    with open(output_csv, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['numero'])
        for number in sorted(unique_numbers):
            writer.writerow([number])

if __name__ == "__main__":
    input_csv = 'clientes.csv'  # Nome do arquivo de entrada
    output_csv = 'numero.csv'  # Nome do arquivo de saída
    extract_unique_mobile_numbers(input_csv, output_csv) """
