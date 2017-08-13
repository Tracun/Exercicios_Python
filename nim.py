def computador_escolhe_jogada(n, m):
	
	if m >= n:
		return n
	else:
		
		#Retorno a sobra de n % (m+1)
		quantRemover = n % (m+1)
		
		if quantRemover > 0:
			return quantRemover;
		else:
			return m;

def usuario_escolhe_jogada(n, m):
	
	pecasRemover = int(input("Quantas peças vai retirar? "))
	
	while pecasRemover > m or pecasRemover <= 0:
		pecasRemover = int(input("Oops ! Jogada inválida ! Quantas peças vai retirar? "))
	
	return pecasRemover

	
def jogo(n,m):
	computerTurn = False
	aux = 0
	
	n = int(input("Quantas peças? "))
	m = int(input("Limite de peças por jogada? "))

	while n < m or n <= 0:
		n = int(input("Oops ! Quantidade inválida ! Quantas peças?"))
		m = int(input("Oops ! Quantidade inválida !Limite de peças por jogada?"))
	
	if (n % (m+1)) != 0:
		computerTurn = True
		print("Computador comeca! ")
	else:
		print("Voce comeca! ")

	while n != 0:
		
		if computerTurn:
			aux = computador_escolhe_jogada(n,m)
			n -= aux
			print("O computador retirou",aux,"pecas.")
			print("Restam", n ,"pecas.")
			computerTurn = False
		else:
			aux = usuario_escolhe_jogada(n,m)
			n -= aux
			print("Voce retirou",aux,"pecas.")
			print("Restam", n ,"pecas.")
			computerTurn = True
	
	if computerTurn:
		print("Voce venceu!")
		return 1
	else:
		print("O computador venceu!")
		return 0
	
def campeonato(n,m):
	aux = 0
	voce = 0
	computer = 0
	
	for i in range(0,3):
		print("**** Rodada", i, "****\n")
		aux = jogo(n,m);
		
		if aux == 0:
			computer += 1
		else:
			voce += 1
			
	print("Placar: Voce", voce,"X", computer, "Computador")
	
	
def partida():
	print("Bem-vindo ao jogo do NUM! Escolha: ")
	
	escolha = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))
	
	if escolha == 1:
		n = 0#int(input("Quantas peças? "))
		m = 0#int(input("Limite de peças por jogada? "))
		jogo(n,m)
	else:
		n = 0#int(input("Quantas peças? "))
		m = 0#int(input("Limite de peças por jogada? "))
		campeonato (n,m)
	
partida()
	
	
	
	
	
