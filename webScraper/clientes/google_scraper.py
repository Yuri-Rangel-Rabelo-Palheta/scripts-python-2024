import requests
from bs4 import BeautifulSoup
import time
import random

def search_google(query, num_pages=10, results_per_page=10, delay_range=(2, 5)):
    base_url = "https://www.google.com/search"
    urls = []

    for page in range(num_pages):
        start_index = page * results_per_page
        params = {
            'q': query,
            'start': start_index,
            'num': results_per_page
        }
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(base_url, headers=headers, params=params)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            for g in soup.find_all('div', class_='yuRUbf'):
                link = g.find('a')['href']
                urls.append(link)
                
            # Adiciona um delay aleatório entre as requisições
            time.sleep(random.uniform(*delay_range))
        else:
            print(f"Erro ao acessar o Google: {response.status_code}")
        
    return urls

