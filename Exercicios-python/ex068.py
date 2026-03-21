"""
Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição de pagamento:

- À vista dinheiro/cheque: 10% de desconto
- À vista cartão: 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
"""

descricao_produto = input("Produto: ").upper() .strip()
preco_produto = float(input("Preço (UN): R$"))
qtd_produto = int(input("Quantidade: "))
forma_pgto = input("Forma de pagamento (1-Din/chq (avista) | 2-Cartão (avista) | 3-Cartão (2x parc) | 4-Cartão (3x parc): ").strip()

valor_produto = preco_produto * qtd_produto


if forma_pgto == "1":
    descricao_pgto = "Dinheiro / Cheque (à vista)"
    desconto = valor_produto * 0.1
    total_pagar = valor_produto  - desconto
elif forma_pgto == "2":
    descricao_pgto = "Cartão (à vista)"
    desconto = valor_produto  * 0.05
    total_pagar = valor_produto  - desconto
elif forma_pgto == "3":
    descricao_pgto = "Cartão (Parcelas em até 2x)"
    total_pagar = valor_produto
    parcela = valor_produto  / 2
elif forma_pgto == "4":
    descricao_pgto = "Cartão (Parcelas em até 3x)"
    juros = valor_produto * 0.2
    total_pagar = valor_produto + juros
    parcela = total_pagar / 3
else: 
    descricao_pgto = "Forma de pagamento invalida"
    total_pagar = 0

print(f"Descrição do Produto: {descricao_produto}")
print(f"Preço: R${preco_produto:.2f}")
print(f"Quantidade: {qtd_produto}")
print(f"Forma de pagamento: {descricao_pgto}")
if forma_pgto == "3":
    print(f"Parcelas: 2x de R${parcela:.2f}")
elif forma_pgto == "4":
    print(f"Parcelas: 3x de R${parcela:.2f}")
print(f"Total a pagar: R${total_pagar:.2f}")        