nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))
media = (nota1 + nota2) / 2

print("")
print("===== FICHA DO ALUNO =====")
print(f"Aluno: {nome_aluno}")
print(f"Nota 1: {nota1:.2f}")
print(f"Nota 2: {nota2:.2f}")
print(f"Média: {media:.2f}")
print("==========================")
