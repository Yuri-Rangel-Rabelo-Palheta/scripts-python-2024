def load_urls_from_file(filename):
    try:
        with open(filename, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
        return urls
    except FileNotFoundError:
        print(f"Arquivo {filename} não encontrado.")
        return []
