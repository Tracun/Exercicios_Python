largura = int(input("Digite a largura do retangulo: "))
altura = int(input("Digite à altura do retangulo: "))

aux = altura
branco = " "
simb = "#"

linhaVazia = simb + (branco * (largura-2)) + simb
linhaCheia = simb * largura

while altura > 0:

        if altura == 1 or altura == aux:
                print(linhaCheia)
        else:
                print(linhaVazia)
        altura -= 1
