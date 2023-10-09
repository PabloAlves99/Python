from classSalvar import adm, CAMINHO
import json

with open(CAMINHO, 'r') as admins:
    adms = json.load(admins)
    
    adm1 = adm(**adms[0])
    adm2 = adm(**adms[1])
    adm3 = adm(**adms[2])
    
    print(vars(adm1))
    print(vars(adm2))
    print(vars(adm3))
    
    