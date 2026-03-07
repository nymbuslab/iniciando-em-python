num_cpf = input("Informe seu cpf (sem pontuação: ")
gp_cpf11 = num_cpf[0:3]
gp_cpf12 = num_cpf[3:6]
gp_cpf13 = num_cpf[6:9]
gp_cpf14 = num_cpf[9:11]

print("\n")
print(f"CPF sem formatação: {num_cpf}")
print(f"CPF formatado: {gp_cpf11}.{gp_cpf12}.{gp_cpf13}-{gp_cpf14}")