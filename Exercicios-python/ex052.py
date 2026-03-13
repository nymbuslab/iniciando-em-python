from datetime import datetime

nome_completo = input("Nome do cliente: ").strip().title()
ano_nascimento = int(input("Informe o ano de nascimento: "))
renda = float(input("Renda: R$"))
score = int(input("Score atual: "))

idade = datetime.now().year - ano_nascimento

if idade < 18 or idade > 70:
    resultado = "Reprovado: Idade fora do intervalo (18-70 anos)"
elif renda <= 1500:
    resultado = "Reprovado: Renda menor que R$1500.00"
elif score < 600:
    resultado = "Reprovado: Score abaixo de 600 pontos"
else:
    resultado = "APROVADO"

print("\n")
print("===== ANÁLISE DE CRÉDITO =====")
print(f"Solicitante: {nome_completo}")
print(f"Idade: {idade}")
print(f"Renda: R${renda:.2f}")
print(f"Score: {score} pontos")
print(f"Resultado: {resultado}")
print("==============================")