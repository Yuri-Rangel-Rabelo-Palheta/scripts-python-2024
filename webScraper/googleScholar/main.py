from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configuração do ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar em modo headless (sem abrir o navegador)
chrome_service = Service('/home/stic/Área de Trabalho/chromedriver-linux64/chromedriver')  # Substitua pelo caminho para o ChromeDriver

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Função para realizar a busca no Google Acadêmico
def busca_google_academico(busca, num_paginas=10):
    # Lista para armazenar os dados
    dados = []

    for pagina in range(num_paginas):
        # Modificar a URL para acessar a página correspondente
        start = pagina * 10
        url = f"https://scholar.google.com/scholar?start={start}&q={busca}&hl=pt-BR&as_sdt=0,5"
        driver.get(url)
        
        # Esperar a página carregar
        time.sleep(3)

        # Extrair o HTML da página
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Encontrar os resultados
        artigos = soup.find_all('div', class_='gs_ri')
        
        # Extrair informações dos artigos
        for artigo in artigos:
            titulo = artigo.find('h3').text
            autores = artigo.find('div', class_='gs_a').text
            link = artigo.find('h3').find('a')['href'] if artigo.find('h3').find('a') else "Link não disponível"
            resumo = artigo.find('div', class_='gs_rs').text if artigo.find('div', class_='gs_rs') else "Resumo não disponível"
            
            dados.append({
                'Título': titulo,
                'Autores': autores,
                'Link': link,
                'Resumo': resumo
            })

    return dados

# Função principal para rodar o scraper
def main(busca, num_paginas=10):
    resultados = busca_google_academico(busca, num_paginas)
    
    # Salvar os resultados em um arquivo CSV
    df = pd.DataFrame(resultados)
    df.to_csv(f'resultados_{busca}.csv', index=False, encoding='utf-8')
    print(f'Resultados salvos em resultados_{busca}.csv')

# Exemplo de uso
if __name__ == "__main__":
    busca = "inteligência artificial"  # Substitua pela string de busca desejada
    main(busca, num_paginas=10)

# Fechar o navegador
driver.quit()




""" from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import pandas as pd
import time

# Configuração do ChromeDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Rodar em modo headless (sem abrir o navegador)
chrome_service = Service('/home/stic/Área de Trabalho/chromedriver-linux64/chromedriver')  # Substitua pelo caminho para o ChromeDriver

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Função para realizar a busca no Google Acadêmico
def busca_google_academico(busca, num_paginas=10):
    # Navegar para o Google Acadêmico
    url = f"https://scholar.google.com/scholar?q={busca}"
    driver.get(url)
    
    # Lista para armazenar os dados
    dados = []

    for pagina in range(num_paginas):
        # Esperar a página carregar
        time.sleep(3)

        # Extrair o HTML da página
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        # Encontrar os resultados
        artigos = soup.find_all('div', class_='gs_ri')
        
        # Extrair informações dos artigos
        for artigo in artigos:
            titulo = artigo.find('h3').text
            autores = artigo.find('div', class_='gs_a').text
            link = artigo.find('h3').find('a')['href'] if artigo.find('h3').find('a') else "Link não disponível"
            resumo = artigo.find('div', class_='gs_rs').text if artigo.find('div', class_='gs_rs') else "Resumo não disponível"
            
            dados.append({
                'Título': titulo,
                'Autores': autores,
                'Link': link,
                'Resumo': resumo
            })

        # Tentar ir para a próxima página
        try:
            next_button = driver.find_element_by_link_text('Próximo')
            next_button.click()
        except:
            print(f"Menos de {num_paginas} páginas disponíveis.")
            break
    
    return dados

# Função principal para rodar o scraper
def main(busca):
    resultados = busca_google_academico(busca)
    
    # Salvar os resultados em um arquivo CSV
    df = pd.DataFrame(resultados)
    df.to_csv(f'resultados_{busca}.csv', index=False, encoding='utf-8')
    print(f'Resultados salvos em resultados_{busca}.csv')

# Exemplo de uso
if __name__ == "__main__":
    busca = "inteligência artificial"  # Substitua pela string de busca desejada
    main(busca)

# Fechar o navegador
driver.quit()
 """