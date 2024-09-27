import csv

def remove_duplicate_numbers(input_file, output_file):
    unique_numbers = set()  # Usando um set para garantir a exclusão de duplicatas

    # Ler o arquivo CSV e coletar os números da coluna 'numero'
    with open(input_file, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            number = row.get('numero')  # Obtém o número da coluna 'numero'
            print("Numero: ",number)
            if number:
                print("Numero dentro do if: ",number)
                unique_numbers.add(number)  # Adiciona o número ao set

    # Salva os números únicos de volta no arquivo CSV
    with open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['numero'])  # Escreve o cabeçalho

        for number in sorted(unique_numbers):  # Grava os números únicos, ordenados
            writer.writerow([number])

# Exemplo de uso:
input_file = 'numeros.csv'
output_file = 'numeros-normais.csv'
remove_duplicate_numbers(input_file, output_file)
