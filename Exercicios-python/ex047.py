from random import random

nome_aluno = input("Nome do aluno: ").strip().title()
ano_nascimento = int(input("Ano de nascimento: "))
turno = input("Informe o turno (Manhã/Tarde/Noite): ").strip()
matricula = (
    nome_aluno.upper()[0:3]
    + str(ano_nascimento)
    + str(int(random() * 100)).zfill(2)
    + turno.upper()[0]
)

print("\n")
print("======= MATRÍCULA =======")
print(f"Aluno: {nome_aluno}")
print(f"Ano Nascimento: {ano_nascimento}")
print(f"Turno: {turno}")
print(f"Matrícula: {matricula}")
print("=========================")
