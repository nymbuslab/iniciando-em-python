"""
Faça um programa que leia o ano de um jovem e informe,
de acordo com a sua idade:

- Se ele ainda vai se alistar ao serviço militar
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

O programa também devera mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date

nome_recruta = input("Digite o nome do candidato: ").strip().title()
ano_nascimento = int(input("Digite o ano de nascimento do candidato: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento


if idade > 18:
    anos_atraso = idade - 18
    if anos_atraso == 1:
        alistamento = f"Você passou 1 ano do prazo"
    else:
        alistamento = f"Você passou {anos_atraso} anos do prazo"
elif idade == 18:
    alistamento = "Está na hora de se alistar! Compareça a junta militar"
else:
    alistamento = f"Você ainda não atende a idade para alistamento militar! Ainda faltam {18 - idade } anos."

print(f"Nome do candidato: {nome_recruta}")
print(f"Idade: {idade} anos")
print(f"Status: {alistamento}")
