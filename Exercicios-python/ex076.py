"""13. Exercício prático do dia a dia
Imagine um cadastro simples de produto em uma loja.

Você precisa guardar:

- nome do produto
- quantidade em estoque
- preço
- se o produto está disponível

Depois, mostrar tudo de forma organizada na tela.
"""
nome_produto = input("Digite o nome do produto: ")
qtd_estoque = int(input("Quantidade em estoque: "))
preco_produto = float(input("Digite o preço do produto: R$"))
disponibilidade_produto = bool(input("Disponível em estoque?:"))

print()
print("======== CADASTRO DE PRODUTO =======")
print(f"Produto: {nome_produto}")
print(f"Estoque: {qtd_estoque}")
print(f"Preço de venda: R${preco_produto:.2f}")
print(f"Disponível para venda: {disponibilidade_produto}")
print("===========================")

"""Exercício 1

Crie 4 variáveis:

uma com texto
uma com número inteiro
uma com número decimal
uma com valor lógico

Depois mostre o valor e o tipo de cada uma usando print() e type()."""

tipo_texto = "Essa variável é do tipo texto: "
tipo_inteiro = 35
tipo_decimal = 1.77
tipo_booleano = False

print(f"{tipo_texto} | {type(tipo_texto)}")
print(f"Essa variável é do tipo inteiro: {tipo_inteiro} | {type(tipo_inteiro)}")
print(f"Essa variável é do tipo inteiro: {tipo_decimal} | {type(tipo_decimal)}")
print(f"Essa variável é do tipo booleano:{tipo_booleano} | {type(tipo_booleano)}")

"""Crie um cadastro simples de pessoa com:

- nome
- idade
- altura
- se está estudando Python

Depois mostre tudo na tela."""

nome_pessoa = input("Digite seu nome: ")
idade_pessoa = int(input("Digite sua idade: "))
altura_pessoa = float(input("Digite sua altura(m): "))
estudando_python = bool(input("Está estudando Python: "))

print()
print("============ CADASTRO PESSOAL ==============")
print(f"Nome completo: {nome_pessoa}")
print(f"Idade: {idade_pessoa} anos")
print(f"Altura: {altura_pessoa:.2f}m")
print(f"Está estudando python: {estudando_python}")
print("===========================================")

"""Exercício 3

Crie um cadastro de produto com:

- nome do produto
- quantidade
- preço
- disponível (True ou False)

Depois mostre os dados organizados."""

nome_produto = input("Digite o nome do produto: ")
qtd_estoque = int(input("Quantidade em estoque: "))
preco_produto = float(input("Digite o preço do produto: R$"))
disponibilidade_produto = bool(input("Disponível em estoque (TrueFalse):"))

print()
print("======== CADASTRO DE PRODUTO =======")
print(f"Produto: {nome_produto}")
print(f"Estoque: {qtd_estoque}")
print(f"Preço de venda: R${preco_produto:.2f}")
print(f"Disponível para venda: {disponibilidade_produto}")
print("===========================")

"""Exercício 4

Escreva um código que mostre a diferença entre:

"10" + "5" e 10 + 5

Mostre os resultados na tela."""

soma_texto1 = input("Digite um número: ")
soma_texto2 = input("Digite um segundo número: ")
soma_numero1 = int(input("Digite novamente um número: "))
soma_numero2 = int(input("Digite novamente um segundo número: "))

resultado_texto = soma_texto1 + soma_texto2
resultado_numero = soma_numero1 + soma_numero2

print(f"O resultado da soma de {soma_texto1} + {soma_texto2} é: {resultado_texto}") #Resposta uma concatenação de string (valores 15 e 20 = 1520)
print(f"O resultado da soma de {soma_numero1} + {soma_numero2} é: {resultado_numero}") #Resposta soma de dois valores inteiros (valores 15 e 20 = 35)