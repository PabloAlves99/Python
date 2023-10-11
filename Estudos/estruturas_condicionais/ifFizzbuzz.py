# Universidade de São Paulo
def fizzbuzz(num):
    if (num % 3 == 0) and (num % 5 != 0):
        return("Fizz")
    elif (num % 3 != 0) and (num% 5 == 0):
        return("Buzz")
    elif (num % 3 == 0) and (num % 5 == 0):
        return("FizzBuzz")
    else:
        return(num)

num = int(input("Digite um número: "))
fizzbuzz(num)