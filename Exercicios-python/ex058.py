"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a 1.250,00, calcule um aumento de 10%.
Para salários superiores inferiores ou iguais, o aumento é de 15%.
"""

salario = float(input('Digite seu salário atual: R$'))


if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

salario_novo = salario + aumento
percentual = 10 if salario > 1250 else 15

print("\n")
print(f'Salário atual: R${salario:.2f}')
print(f'Aumento de: {percentual}%')
print(f'Valor de reajuste: R${aumento:.2f}')
print(f'Novo salário: R${salario_novo:.2f}')