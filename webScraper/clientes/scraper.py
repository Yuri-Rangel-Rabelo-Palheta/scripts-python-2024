import requests  # Adicione esta linha
from requests.exceptions import RequestException
from selenium_scraper import fetch_page_content_with_selenium

def fetch_page_content(url, use_selenium=False):
    if use_selenium:
        return fetch_page_content_with_selenium(url)
    else:
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.text
        except RequestException as e:
            print(f"Erro ao acessar a URL: {e}")
            return None
