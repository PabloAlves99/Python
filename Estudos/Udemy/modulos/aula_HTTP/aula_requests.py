import requests

URL = 'http://127.0.0.1:5500/Estudos/Udemy/modulos/aula_HTTP/index.html'
response = requests.get(URL, timeout=5)

print(response.headers)
