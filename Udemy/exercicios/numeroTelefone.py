import random

def create_phone_number(n):   
    if len(n) != 10:
        return('Digite apenas 10 números')
    else:
        return '({}{}{}) {}{}{}-{}{}{}{}'.format(*n)
#       n.insert(0,'(')
#        n.insert(4,')')
#        n.insert(5, ' ')
#        n.insert(9, '-')

#        numberForm = ''
#        for i in n:
#            numberForm += str(i)

#    return numberForm
 
n = []
for i in range(10):
    n.append(random.randint(0,9))

print(create_phone_number(n))
