'''
Escreva um programa que faça o computador "pensar" em um número entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário acertou ou não.
'''

from random import randint

num_aleatorio = randint(0, 5)
num_escolhido = int(input('Digite um número de 0 a 5: '))

if num_escolhido < 0 or num_escolhido > 5:
    resultado = 'Número inválido! Digite entre 0 e 5.'
elif num_escolhido == num_aleatorio:
    resultado = 'Você acertou!'
else:
    resultado = 'Você errou, tente novamente!'
    
print('\n')
print('===== NÚMERO SECRETO =====')
print(resultado)
print(f'O número secreto foi: {num_aleatorio}')
print(f'Você escolheu o número: {num_escolhido}')
print('==========================')

