import os
from PyPDF2 import PdfReader, PdfWriter

# Função para mesclar PDFs
def merge_pdfs(input_folder, output_filename):
    # Lista todos os arquivos PDF na pasta e ordena em ordem alfabética
    pdf_files = sorted([f for f in os.listdir(input_folder) if f.endswith('.pdf')])

    # Inicializa o writer para o novo PDF
    pdf_writer = PdfWriter()

    # Para cada arquivo PDF, ler e adicionar as páginas ao writer
    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_folder, pdf_file)
        pdf_reader = PdfReader(pdf_path)

        # Adiciona cada página ao writer
        for page_num in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page_num])

    # Grava o PDF final mesclado
    with open(output_filename, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f"PDFs mesclados em: {output_filename}")

# Caminho da pasta contendo os PDFs e nome do arquivo de saída
input_folder = "."  # Substitua pelo caminho da sua pasta
output_filename = "documento_final.pdf"  # Nome do arquivo final

# Chama a função para mesclar os PDFs
merge_pdfs(input_folder, output_filename)
