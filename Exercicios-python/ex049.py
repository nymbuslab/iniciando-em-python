from datetime import datetime

nome = input("Nome completo: ").strip().title()
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = datetime.now().year
idade = ano_atual - ano_nascimento

if idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print("\n")
print(f"Nome: {nome}")
print(f"Idade: {idade} anos")
print("================")
print(f"Nome: {nome}")
print(f"Classificação: {classificacao}")
print("================")
