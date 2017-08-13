n1 = int(input("Digite a cordenada 'X': "))
n2 = int(input("Digite a cordenada 'Y': "))

n3 = int(input("Digite a cordenada 'X' de outro plano: "))
n4 = int(input("Digite a cordenada 'X' de outro plano: "))

if ((n3 - n1) >= 10) or ((n4 - n2) >= 10):
    print("longe")
else:
    print("perto")

