import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

def init_driver():
    chrome_driver_path = r"C:\Users\yurim\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Substitua pelo caminho real do chromedriver.exe
    
    service = Service(chrome_driver_path)
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def extract_contact_info(driver, profile_url):
    driver.get(profile_url)
    time.sleep(5)  # Espera para garantir que a página carregue completamente

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    try:
        # Extrair nome
        name = soup.find('li', class_='inline t-24 t-black t-normal break-words').get_text(strip=True)

        # Extrair email e telefone (se estiverem disponíveis no perfil)
        contact_info_section = soup.find('section', class_='pv-contact-info__contact-type ci-email')
        email = contact_info_section.find('a').get_text(strip=True) if contact_info_section else "Não disponível"

        phone_section = soup.find('section', class_='pv-contact-info__contact-type ci-phone')
        phone = phone_section.find('span', class_='t-14 t-black t-normal').get_text(strip=True) if phone_section else "Não disponível"

        return {'name': name, 'email': email, 'phone': phone, 'link': profile_url}
    except Exception as e:
        print(f"Erro ao extrair informações de contato do perfil: {e}")
        return None

def search_linkedin(query, num_pages=5, results_per_page=10, delay_range=(2, 5)):
    base_url = "https://www.linkedin.com/search/results/people/"
    profile_data = []

    driver = init_driver()

    for page in range(num_pages):
        start_index = page * results_per_page
        params = {
            'keywords': query,
            'start': start_index
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept-Language': 'en-US,en;q=0.9',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        }

        response = requests.get(base_url, headers=headers, params=params)
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Encontrar e extrair links dos perfis
            for profile in soup.find_all('div', class_='entity-result__item'):
                try:
                    link = profile.find('a', class_='app-aware-link')['href']
                    if '/in/' in link:  # Verifica se é um link de perfil
                        contact_info = extract_contact_info(driver, link)
                        if contact_info:
                            profile_data.append(contact_info)
                
                except Exception as e:
                    print(f"Erro ao extrair dados do perfil: {e}")
                
            # Adiciona um delay aleatório entre as requisições
            time.sleep(random.uniform(*delay_range))
        else:
            print(f"Erro ao acessar o LinkedIn: {response.status_code}")
        
    driver.quit()
    return profile_data

