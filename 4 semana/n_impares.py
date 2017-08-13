num = int(input("Digite um numero inteiro positivo: "))

while num < 0:
    num = int(input("Número inválido, digite um numero inteiro positivo: "))

i = 0

while num != 0:
    if(i % 2) != 0:
        print(i)
        num -= 1
        i = i + 1

    i = i + 1

