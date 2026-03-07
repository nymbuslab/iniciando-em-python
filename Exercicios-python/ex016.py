'''
Crie um programa que leia quanto dinheiro ela tem na carteira e mostre quantos dólares ela pode comprar
'''

dinheiro_carteira = float(input("Quanto você tem na carteira? R$:"))
cotacao_dolar = 5.18
conversao_real = dinheiro_carteira / cotacao_dolar

print("Dinheiro disponível: R$", dinheiro_carteira)
print("Cotação atual do dólar: U$", cotacao_dolar)
print("Quanto você pode comprar em dólar: U$", conversao_real)