nome_cliente = input("Digite o nome do cliente: ")
nome_produto = input("Digito nome do produto: ")
preco_unitario = float(input("Valor do produto: R$"))
quantidade_comprada = int(input("Quantidade: "))
total_compra = preco_unitario * quantidade_comprada

print()
print("========= RECIBO =========")
print(f"Cliente: {nome_cliente}")
print(f"Produto: {nome_produto}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Quantidade: {quantidade_comprada}")
print(f"Total: R${total_compra:.2f}")
print("=========================")

nome_diarista = input("Diarista cadastrada: ")
valor_diaria = float(input("Valor da diária: R$"))
dias_trabalhados = int(input("Quantidade de dias trabalhados: "))
valor_receber = valor_diaria * dias_trabalhados

print()
print("===== PAGAMENTO =====")
print("Diarista: {}".format(nome_diarista))
print("Valor da diária: R$ {:.2f}".format(valor_diaria))
print("Dias trabalhados: {}".format(dias_trabalhados))
print("Total a receber: R$ {:.2f}".format(valor_receber))
print("=====================")


print("============= CONVERSOR DE REAIS/DÓLAR =============")
valor_real = float(input("Digite o valor em reais: R$ "))
cotacao_dolar = float(input("Informe a cotação atual do dólar: U$ "))
total_convertido = valor_real / cotacao_dolar

print("------------------------------------------")
print("Valor disponível para compra: R$ {:.2f}".format(valor_real))
print(f"Cotação do dólar atual: U$ {cotacao_dolar:.2f}")
print(f"Você pode comprar o total de U$ {total_convertido:.2f}")

titulo = " SISTEMA DE VENDAS "
print(f"{titulo:=^40}")

nome_aluno = input("Digite o nome do aluno: ")
curso = input("Cursando: ")
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))
media = (nota1 + nota2) / 2
print()
print("Nome do aluno: {}".format(nome_aluno))
print("Curso: {}".format(curso))
print(f"A primeira nota do aluno foi {nota1:.2f} e a segunda {nota2:.2f}, então sua média final é: {media:.2f}")

titulo = " ORÇAMENTO "
nome_cliente2 = input("Informe o nome do cliente: ")
servico_prestado = input("Serviço prestado: ")
valor_mao_obra = float(input("Valor da mão de obra: R$"))
valor_pecas = float(input("Valor total das peças: R$"))
total_servico = valor_mao_obra + valor_pecas

print(f"{titulo:=^33}")
print(f"Cliente: {nome_cliente2}")
print(f"Serviço: {servico_prestado}")
print(f"Mão de obra: R${valor_mao_obra:.2f}")
print(f"Peças: R${valor_pecas:.2f}")
print(f"Total do serviço: R${total_servico:.2f}")
print("=================================")