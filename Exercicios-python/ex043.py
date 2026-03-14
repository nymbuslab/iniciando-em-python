nome_cliente = input("Nome do cliente: ").strip().title()
nome_produto = input("Produto: ").strip().title()
preco_unitario = float(input("Preço do produto (Un): R$"))
quantidade_item = int(input("Quantidade: "))
desconto = int(input("Desconto a vista: "))

subtotal = preco_unitario * quantidade_item
valor_desconto = subtotal * desconto / 100
print("\n")
print("========= RECIBO =========")
print(f"Cliente: {nome_cliente}")
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Quantidade: {quantidade_item}")
print(f"Subtotal: R${subtotal:.2f}")
print(f"Desconto ({desconto}%): R${valor_desconto:.2f}")
print(f"Total: R${subtotal - valor_desconto:.2f}")
print("==========================")
