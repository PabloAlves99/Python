from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(ChromeDriverManager().install()) # Instalar o ChromeDriver na versão atual

navegador = webdriver.Chrome(service= service)
navegador.get('https://www.selenium.dev/pt-br/documentation/')
