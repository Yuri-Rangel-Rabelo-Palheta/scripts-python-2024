from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

def extract_company_data(company_element):
    """Extrai e valida os dados de uma empresa a partir do elemento HTML.

    Args:
        company_element: Elemento HTML representando uma empresa.

    Returns:
        Tupla contendo nome, telefone e site da empresa, ou None se os dados não forem válidos.
    """

    try:
        # Extrair e validar o nome (deve começar com letra maiúscula)
        print("Tentando extrair nome da empresa...")
        name = company_element.find('div').text.strip()
        if not re.match(r'^[A-ZÀ-Ý]', name):
            print(f"Nome inválido: {name}")
            #return None, None, None

        # Extrair e validar o telefone (ex: (XX) XXXXX-XXXX)
        phone = company_element.find('span').text.strip()
        print("Telefones:", phone)
        if not re.match(r'^\(\d{2}\) \d{4,5}-\d{4}$', phone):
            print(f"Telefone inválido: {phone}")
            #return None, None, None

        # Extrair e validar o site (deve conter 'http' ou 'https')
        website = company_element.find('a')
        print("Website:", website)
        website = website['href'] if website and 'http' in website['href'] else 'N/A'

        return name, phone, website
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return None, None, None

def scrape_google_local_services(search_term, output_file='empresas.csv'):
    """Realiza o scraping de dados de empresas no Google Local Services.

    Args:
        search_term: Termo de pesquisa.
        output_file: Nome do arquivo CSV para salvar os resultados.
    """

    # Configuração do WebDriver
    chrome_driver_path = r"C:\Users\yurim\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Substitua pelo caminho real do chromedriver.exe
    
    service = Service(chrome_driver_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Acessa a página e realiza a pesquisa
        driver.get("https://www.google.com/maps/search/")
        try:
            search_bar = WebDriverWait(driver, 20).until(  # Aumentou o timeout
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']"))
            )
            search_bar.send_keys(search_term)
            search_bar.submit()
        except TimeoutException:
            print("Erro: Tempo limite excedido ao encontrar a barra de pesquisa.")
            return

        # Extrai dados da primeira página
        time.sleep(5)  # Ajuste o tempo de espera conforme necessário
        html_content = driver.page_source
        soup = BeautifulSoup(html_content, 'html.parser')
        companies = soup.find_all('div')  # Ajuste o seletor se necessário

        # Salva os dados em um arquivo CSV
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['Nome', 'Telefone', 'Site']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for company in companies:
                print("Tentando extrair dados")
                name, phone, website = extract_company_data(company)
                if name and phone:  # Verifica se os dados foram extraídos com sucesso
                    writer.writerow({'Nome': name, 'Telefone': phone, 'Site': website})

    except (NoSuchElementException, TimeoutException) as e:
        print(f"Erro durante o scraping: {e}")
    finally:
        driver.quit()

# Exemplo de uso:
search_term = "advogados em belém"
scrape_google_local_services(search_term)
