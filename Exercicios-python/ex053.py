"""
Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário acertou ou não.
"""

from random import randint
from time import sleep
computador = randint(0, 5)
jogador = int(input("Digite um número de 0 a 5: "))

if jogador < 0 or jogador > 5:
    resultado = "Número inválido! Digite entre 0 e 5."
elif jogador == computador:
    resultado = "Você acertou!"
else:
    resultado = "Você errou, tente novamente!"

print("\n")
print("===== NÚMERO SECRETO =====")
print(f"Você escolheu o número: {jogador}")
print('PROCESSANDO...')
sleep(3)
print(f'{resultado}')
print(f"O número secreto foi: {computador}")
print("==========================")
