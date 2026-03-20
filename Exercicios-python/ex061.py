"""
Escreva um programa para aprovar o empréstimo bancário para a
compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.

Calcule o valor da prestação, sabendo que ela não pode exceder 30% do salário ou
então o empréstimo será negado
"""

valor_imovel = float(input("Qual o valor do imóvel para financiamento: R$"))
renda_pessoal = float(input("Qual o valor da renda pessoal: R$"))
parcelamento = int(input("Em quandos anos vamos parcelar: "))

prestacao = valor_imovel / (parcelamento * 12)
limite_salario = renda_pessoal * 0.3

if prestacao <= limite_salario:
    credito = "APROVADO"
else:
    credito = f"REPROVADO - Prestação R${prestacao:.2f} excede 30% da renda"

print("\n")
print(f"Valor do imóvel: R${valor_imovel:.2f}")
print(f"Renda pessoal: R${renda_pessoal:.2f}")
print(f"Parcelamento (anos): {parcelamento} anos")
print(f"Valor da prestação: R${prestacao:.2f}")
print(credito)
