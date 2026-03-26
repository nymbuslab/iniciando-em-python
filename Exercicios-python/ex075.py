#1 - Crie um programa que mostre a frase: "Olá, seja bem-vindo ao Python!"
saudacao = "Olá, seja bem-vindo ao Python!"
print(saudacao)

#2 - Crie uma variável com seu nome e mostre na tela uma mensagem de apresentação.
nome = "Pabllo"
print("Olá, meu nome é " + nome)

#3 - Crie um programa que peça ao usuário:
# nome
# cidade
nome2 = input("Digite o seu nome: ")
cidade = input("Agora, a sua cidade: ")

print("Seu nome é " + nome2)
print("Você mora em " + cidade)

#4 - Crie um programa que peça ao usuário o nome de um produto e depois mostre:
# Produto informado:...

produto = input("Informe a descrição do produto: ")
print("Produto informado: " + produto)

#5 - Crie um mini cadastro que peça:

# nome
# telefone
# cidade

#Depois mostre todos os dados na tela.

nome3 = input("Digite o nome completo: ")
telefone = input("Agora o número de telefone (xx)x xxxx-xxxx: ")
cidade2 = input("E por sim, a cidade: ")

print("\n")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("       CADASTRO PESSOAL      ")
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Nome: " + nome3)
print("Telefone: " + telefone)
print("Cidade: " + cidade2)
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")

#6 - Imagine um atendimento de loja.
#Crie um programa que peça:

#nome do cliente
#produto de interesse

nome_cliente = input("Digite o nome do cliente: ")
produto2 = input("Qual o produto de interesse: ")

print("Nome do cliente: " + nome_cliente)
print("Produto de interesse: " + produto2)

#Imagine um atendimento simples de oficina ou loja.
#Crie um programa que peça:

#nome do cliente
#serviço desejado
#cidade

#Depois mostre assim:

#===== ATENDIMENTO =====
#Cliente: ...
#Serviço: ...
#Cidade: ...
#======================

nome_cliente = input("Informe o nome do cliente: ")
servico = input("Serviço solicitado: ")
cidade_cliente = input("Informa cidade do cliente: ")

print()
print("===== ATENDIMENTO =====")
print("Cliente: " + nome_cliente)
print("Serviço: " + servico)
print("Cidade: " + cidade_cliente)
print("======================")

"""
Saida:
===== ATENDIMENTO =====
Cliente: João Carlos
Serviço: Troca de Pneus
Cidade: Sales Oliveira
======================
"""
