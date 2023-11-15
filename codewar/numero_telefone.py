import random


def create_phone_number(n):
    if len(n) != 10:
        print('Digite exatos 10 números')
    else:
        return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)


n = []
for i in range(10):
    n.append(random.randint(0, 9))

print(create_phone_number(n))
