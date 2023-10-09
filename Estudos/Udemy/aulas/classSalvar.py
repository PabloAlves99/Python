import json

CAMINHO = "loginAdm.json"

class adm:
    master = 'Pablo'
    def __init__(self, administrador, chave):
        self.administrador = administrador
        self.chave = chave
   
ad1 = adm('Pablo', 123)
ad2 = adm('Henrique', 456)
ad3 = adm('Alves', 789)

adms = [ad1.__dict__, vars(ad2), ad3.__dict__]
if __name__ == '__main__':
    print(adms)
    with open(CAMINHO, "w+", encoding='utf8') as admins:
        json.dump(adms, admins, indent=2, ensure_ascii=False)

