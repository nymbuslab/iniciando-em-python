"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
"""

nome_completo = input("Digite o nome completo: ")

print(f"Nome completo digitado: {nome_completo}")
print(f"Primeiro nome: {nome_completo.split()[0] .title()}")
print(f"Último nome: {nome_completo.split()[-1] .title()}")
