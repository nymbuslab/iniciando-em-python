"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
ex: Digite um número: 6.127, o número 6.127 tem a parte inteira 6
"""

import math

num_qualquer = float(input("Digite um número real(com casas decimais): "))


"""
trunc elimina os números após a virgula, trazendo apenas parte inteira
"""
print(f"A parte inteira de {num_qualquer} é: {math.trunc(num_qualquer)}")
