"""
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida.
"""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print(f"Parabéns! Sua média foi {media:.2f}")
    print("STATUS: APROVADO")
elif media >= 5:
    print(f"EM ANÁLISE! Sua média foi {media:.2f}")
    print("STATUS: RECUPERAÇÃO")
else:
    print(f"SINTO MUITO! Sua média foi {media:.2f}")
    print("STATUS: REPROVADO")

