def soma_hipotenusas(n):
    def e_triangulo_retangulo(a, b, c):
        return a ** 2 + b ** 2 == c ** 2

    soma = 0

    for hipotenusa in range(1, n + 1):
        for cateto1 in range(1, hipotenusa):
            cateto2 = (hipotenusa ** 2 - cateto1 ** 2) ** 0.5
            if cateto2 == int(cateto2) and e_triangulo_retangulo(cateto1, int(cateto2), hipotenusa):
                soma += hipotenusa
                break

    return soma


numero = int(input("Digite um valor: ")) # type: ignore
resultado = soma_hipotenusas(numero)
print(f"A soma das hipotenusas até {numero} é: {resultado}")
