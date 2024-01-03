# pylint: disable= missing-docstring
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Instalar o ChromeDriver na versão atual
service = Service(ChromeDriverManager().install())

# Inicializar o navegador
navegador = webdriver.Chrome(service=service)
navegador.get('https://www.google.com.br/')

# Localizar o elemento de pesquisa pelo ID
search = navegador.find_element(By.ID, 'APjFqb')

# Inserir texto no campo de pesquisa
search.send_keys('Cruzeiro')

# Pressionar Enter
search.send_keys(Keys.ENTER)
search = navegador.find_element(By.ID, 'sports-app')
search.click()
sleep(5)

# Fechar o navegador
navegador.quit()
