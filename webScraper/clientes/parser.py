from bs4 import BeautifulSoup
import re
import csv

def parse_client_data(html_content, site_name=None):
    soup = BeautifulSoup(html_content, 'html.parser')
    clients = []

    # Padrões de Regex para identificar emails e números de telefone
    email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-z0-9-]+\.[a-z0-9-.]+')
    phone_pattern = re.compile(r'\(?\+?[0-9]{1,4}\)?[-.\s]?[0-9]{2,4}[-.\s]?[0-9]{3,4}[-.\s]?[0-9]{3,4}')

    # Procurar emails
    emails = set(email_pattern.findall(soup.get_text()))

    # Procurar números de telefone
    phones = set(phone_pattern.findall(soup.get_text()))

    # Procurar nomes de empresas ou pessoas
    # Supondo que nomes estejam em tags específicas como <h1>, <h2>, <h3>
    names = [tag.get_text().strip() for tag in soup.find_all(['h1', 'h2', 'h3'])]

    #addresses = [tag.get_text().strip() for tag in soup.find_all('address')]

    # Se não encontrar nomes, use o nome do site como fallback
    if not names and site_name:
        names.append(site_name)

    # Combinações simples para gerar objetos de clientes
    for name in names:
        for email in emails:
            for phone in phones:
                client = {
                    'name': name,
                    #'site_name': site_name,
                    'email': email,
                    'phone': phone
                }
                clients.append(client)

    # Remover duplicatas caso algum cliente seja duplicado
    clients = [dict(t) for t in {tuple(d.items()) for d in clients}]
    
    return clients



""" from bs4 import BeautifulSoup
import re

def parse_client_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    clients = []

    # Padrões de Regex para identificar emails e números de telefone
    email_pattern = re.compile(r'[\w\.-]+@[\w\.-]+')
    phone_pattern = re.compile(r'\(?\+?[0-9]{1,4}\)?[-.\s]?[0-9]{2,4}[-.\s]?[0-9]{3,4}[-.\s]?[0-9]{3,4}')

    # Procurar emails
    emails = set(email_pattern.findall(soup.get_text()))

    # Procurar números de telefone
    phones = set(phone_pattern.findall(soup.get_text()))

    # Procurar nomes de empresas ou pessoas
    # Supondo que nomes estejam em tags específicas como <h1>, <h2>, <h3>
    names = [tag.get_text().strip() for tag in soup.find_all(['h1', 'h2', 'h3'])]

    # Extração adicional (e.g., endereços, cargos)
    # Isso pode variar conforme o site
    # Example: addresses = [tag.get_text().strip() for tag in soup.find_all('address')]

    # Combinações simples para gerar objetos de clientes
    for name in names:
        for email in emails:
            for phone in phones:
                client = {
                    'name': name,
                    'email': email,
                    'phone': phone
                }
                clients.append(client)

    # Remover duplicatas caso algum cliente seja duplicado
    clients = [dict(t) for t in {tuple(d.items()) for d in clients}]
    
    return clients

 """