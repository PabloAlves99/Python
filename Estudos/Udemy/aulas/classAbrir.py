# Udemy com Luiz Otávio Miranda
from classSalvar import users, CAMINHO
import json

with open(CAMINHO, 'r') as arquivo:
    
    list_users = json.load(arquivo)   
    user1 = users.create_full_user(**list_users[0])
    user2 = users.create_full_user(**list_users[1])
    
print(vars(user1))
print(vars(user2))
    
    