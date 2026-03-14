"""
Faça um programa que leia um ano qualquer e meste se ele é bissexto
"""

ano = int(input("Digite um ano qualquer: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano BISSEXTO!")
else:
    print(f"{ano} nào é um ano BISSEXTO!")
