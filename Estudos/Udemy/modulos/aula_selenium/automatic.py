# Selenium - Automatizando tarefas no navegador
# pylint: disable=missing-docstring
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


# Chrome Options
# https://peter.sh/experiments/chromium-command-line-switches/


def make_chrome_browser(*_options: str) -> webdriver.Chrome:
    # pylint: disable=missing-docstring

    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if _options is not None:
        for option in _options:
            chrome_options.add_argument(option)  # type: ignore

    # Instalar o ChromeDriver na versão atual
    chrome_service = Service(ChromeDriverManager().install())

    chrome_browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return chrome_browser


if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Como antes
    browser.get('https://www.google.com')

    # Dorme por 10 segundos
    sleep(10)
