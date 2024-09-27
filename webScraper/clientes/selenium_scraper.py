from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def init_driver():
    chrome_driver_path = r"C:\Users\yurim\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"  # Substitua pelo caminho real do chromedriver.exe
    
    service = Service(chrome_driver_path)
    #service = Service("/usr/bin/chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    #chrome_options=webdriver.ChromeOptions() 
    chrome_options.add_experimental_option('excludeSwitch',['enable-logging']) 
    chrome_options.add_argument('--log-level=3') 
    #driver=webdriver.Chrome(executable_path='C:\Users\yurim\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe', options=chrome_options)

    chrome_options=webdriver.ChromeOptions() 
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def fetch_page_content_with_selenium(url):
    driver = init_driver()
    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content