from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# Instalar o ChromeDriver na versão atual
service = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=service)
navegador.get('https://www.selenium.dev/pt-br/documentation/')
