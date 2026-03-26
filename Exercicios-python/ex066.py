"""
A Confederação Nacional de Natação precisa de um programa
que leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:

- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
"""

from datetime import date

ano_nascimento = int(input("Digite o ano de nascimento do atleta: "))
idade = date.today().year - ano_nascimento

if idade <= 0:
    categoria = "Sem categoria — idade inválida"
elif idade <= 9:
    categoria = "MIRIM"
elif idade <= 14:
    categoria = "INFANTIL"
elif idade <= 19:
    categoria = "JUNIOR"
elif idade == 20:
    categoria = "SÊNIOR"
else:
    categoria = "MASTER"

print(f"Idade do participante: {idade} anos")
print(f"Categoria: {categoria}")