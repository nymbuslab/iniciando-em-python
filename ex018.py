'''
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
'''

preco_prod = float(input("Digite o preço do produto R$:"))
desconto = preco_prod * 0.05 

print("Preço sem desconto: R$", preco_prod)
print("Preço com desconto,", preco_prod - desconto)