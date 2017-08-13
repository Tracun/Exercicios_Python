n = int(input("Digite um numero a ser fatorado: "))

fatorial = 1

while n > 0:
    fatorial =  fatorial * n
    n = n - 1

print(fatorial)
