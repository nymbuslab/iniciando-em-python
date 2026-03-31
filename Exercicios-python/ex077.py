"""
## Exercício 1 — cálculo simples

Peça dois números inteiros ao usuário e mostre:

- soma
- subtração
- multiplicação
- divisão
"""


numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print(f"O resultado da soma entre {numero1} + {numero2}: {numero1 + numero2}")
print(f"A diferença da subtração entre {numero1} + {numero2}: {numero1 + numero2}")
print(f"O produto da multiplicação entre {numero1} + {numero2}: {numero1 + numero2}")
print(f"O quociente da divisão entre {numero1} + {numero2}: {numero1 + numero2}")

"""
## Exercício 2 — situação real: compra

Peça:

- nome do produto
- preço unitário
- quantidade

Depois mostre:

- nome do produto
- valor unitário
- quantidade
- valor total da compra
"""
nome_produto = input("Digite o nome do produto: ")
valor_produto = float(input("Valor do produto: R$"))
quantidade_venda = int(input("Quantidade: "))

total_compra = valor_produto * quantidade_venda

print()
print("=========== CUPOM DO PEDIDO ===========")
print(f"Nome do produto: {nome_produto}")
print(f"valor: {valor_produto:.2f}")
print(f"Quantidade: {quantidade_venda}")
print(f"Total da compra: {total_compra:.2f}")
print("========================================")

"""
Exercício 3 — situação real: salário

Peça o salário mensal de uma pessoa e o valor das despesas do mês.

Depois mostre:

salário
despesas
valor restante
"""

nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Informe o salário: R$"))
despensa_mes = float(input("Valor total das despesa mensal: R$"))

valor_restante = salario - despensa_mes

print()
print(f"Identificação funcionário? {nome_funcionario}")
print(f"Salário: R${salario:.2f}")
print(f"Total de despesa: R${despensa_mes:.2f}")
print(f"Valor Restante: R${valor_restante:.2f}")

"""
Exercício 4 — resto da divisão

Peça um número ao usuário e mostre:

o resultado da divisão dele por 2
o resto da divisão por 2
"""

numero_divisor = int(input("Digite um número: "))

resultado = numero_divisor // 2
resto_divisao = resultado % 2

print(f"Resultado da divisão do número {numero_divisor} por 2 é {resultado}")
print(f"E o resto da {resultado} divido po 2 é {resto_divisao}")

"""Exercício 5 — potência

Peça um número ao usuário e mostre:

o quadrado dele
o cubo dele"""

numero_potencia = int(input("Digite um número: "))

resultado_quadrado = numero_potencia ** 2
resultado_cubo = numero_potencia ** 3

print()
print(f"O número {numero_potencia} elevado ao quadrado é: {resultado_quadrado}")
print(f"O número {numero_potencia} elevado ao cubo é: {resultado_cubo}")

"""
8. Exercício de situação real mais completo
Situação: caixa de loja

Crie um programa que peça:

nome do produto
preço unitário
quantidade comprada
valor pago pelo cliente

Depois calcule e mostre:

total da compra
troco do cliente
"""

nome_produto = input("Digite o nome do produto: ")
preco_unitario = float(input("Informe o valor do produto: R$"))
quantidade_comprada = int(input("Informe a quantidade comprada: "))
total_compra = preco_unitario * quantidade_comprada
valor_pago = float(input("Valor pago: R$"))
troco_cliente = valor_pago - total_compra

print("===== RESUMO DA COMPRA =====")
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Quantidade: {quantidade_comprada}")
print(f"Total: R${total_compra:.2f}")
print(f"Valor pago: R${valor_pago:.2f}")
print(f"Troco: R${troco_cliente:.2f}")
print("===========================")