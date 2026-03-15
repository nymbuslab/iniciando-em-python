"""
Desenvolva um programa que pergunte a distancia de uma
viagem em km.
Calcule o preço da passagem, cobrando R$0.50 por km para viagens de até 200km
e R$0.45 para viagens mais longas.
"""

distancia_viagem = float(input("Digite a distância da viagem em km: "))

if distancia_viagem <= 0:
    preco_passagem = "Distância inválida"
elif distancia_viagem <= 200:
    preco_passagem = distancia_viagem * 0.50
else:
    preco_passagem = distancia_viagem * 0.45

print("\n")
if isinstance(preco_passagem, str):
    print(preco_passagem)
else:
    print(f"Distância da viagem: {distancia_viagem:.2f}km")
    print(f"Preço da passagem: R${preco_passagem:.2f}")
