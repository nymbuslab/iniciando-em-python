"""
005 - 
Escreva um programa que:

1. Peça o nome do usuário
2. Peça o preço de um produto (número com decimal)
3. Peça a quantidade (número inteiro)
4. Calcule o total (preço x quantidade)
5. Exiba a saída nesse formato:

Produto comprado por: Carlos
Preço unitário: 9.5
Quantidade: 3
Total: 28.5
"""

nome = input("Digite seu usuário: ")
preco_produto = float(input("Digite o preço do produto: "))
qtd_produto = int(input("Digite a quantidade: "))
total_compra = preco_produto * qtd_produto

print(f"Produto comprado por {nome}")
print(f"Preço unitário: R${preco_produto:.2f}")
print(f"Quantidade: {qtd_produto}")
print(f"Total: R${total_compra:.2f}")