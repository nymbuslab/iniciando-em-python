import random

jogador1 = input("Jogador 1: ")
jogador2 = input("Jogador 2: ")
jogador3 = input("Jogador 3: ")
jogador4 = input("Jogador 4: ")

sorteio = random.randint(1, 4)

'''
Solução usando if
'''
'''if sorteio == 1:
  print(f"O capitão sorteado é: {jogador1}")
if sorteio == 2:
  print(f"O capitão sorteado é: {jogador2}")
if sorteio == 3:
  print(f"O capitão sorteado é: {jogador3}")
if sorteio == 4:
  print(f"O capitão sorteado é: {jogador4}")
  '''
  
capitao = [jogador1, jogador2, jogador3, jogador4]
escolhido = random.choice(capitao)

print(f"O capitão sorteado é: {escolhido}")
