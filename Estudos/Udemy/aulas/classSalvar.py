import json

CAMINHO = "login_users.json"

class users:   
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None
   
    def set_user(self, user):
        self.user = user
        
    def set_password(self, password):
        self.password = password

    @classmethod
    def create_full_user(cls, user, password, host):
        user_full = cls()
        user_full.user = user
        user_full.password = password
        user_full.host = host
        
        return user_full
        
user1 = users()
user2 = users()

user1.set_user('Pablo')
user1.set_password('123')

user2.set_user('Alves')
user2.set_password('456')

list_users =[vars(user1), user2.__dict__]
if __name__ == '__main__':

    with open(CAMINHO, "w+", encoding='utf8') as admins:
        json.dump(list_users, admins, indent=2, ensure_ascii=False)
