nome_aluno = input("Nome do aluno: ")
plano = input("Plano contratado: ")
valor_mensal = float(input("Valor da mensalidade: R$"))
valor_desconto = valor_mensal * 0.10
total_pagar = valor_mensal - valor_desconto
print("")
print("======= ACADEMIA FIT =======")
print(f"Aluno: {nome_aluno}")
print(f"Plano: {plano}")
print(f"Valor: {valor_mensal:.2f}")
print(f"Desconto à vista (10%): {valor_desconto:.2f}")
print(f"Total à vista: {total_pagar:.2f}")
print("============================")