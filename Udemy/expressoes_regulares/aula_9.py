import re
from pprint import pprint


texto = '''
ONLINE  192.168.0.1 GHIJK active
OFFLINE  192.168.0.2 GHIJK inactive
OFFLINE  192.168.0.3 GHIJK active
ONLINE  192.168.0.4 GHIJK active
ONLINE  192.168.0.5 GHIJK inactive
OFFLINE  192.168.0.6 GHIJK active
'''

# # Positive lookahead
pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))  # noqa

# # Negative lookahead
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))  # noqa

# # Positive lookahead
# pprint(re.findall(r'(?=.*[^in]active).+', texto))
# # [ ^ in]: Corresponde a qualquer caractere que não seja "i" ou "n".
# # active: Corresponde literalmente à sequência "active".


# # Positive lookbehind
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))  # noqa
# # (?<= ONLINE): Este é um lookbehind positivo que verifica se a sequência
# # "ONLINE" ocorre imediatamente antes do padrão correspondente. No entanto,
# # o conteúdo correspondente ao lookbehind positivo não é incluído na
# # correspondência.

# # Negative lookbehind
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))  # noqa

# # Positive lookbehind
# pprint(re.findall(r'\w+(?<=OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))  # noqa

# # Negative lookbehind
# pprint(re.findall(r'\w+(?<!OFFLINE)\s+\d+\.\d+\.\d+\.\d+\s+\w+\s+\w+', texto))  # noqa
