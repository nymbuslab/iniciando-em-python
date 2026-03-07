import random

nome_usuario = input("Digite seu usuário: ")
digito_senha1 = random.randint(0, 9)
digito_senha2 = random.randint(0, 9)
digito_senha3 = random.randint(0, 9)
digito_senha4 = random.randint(0, 9)
senha = str(digito_senha1) + str(digito_senha2) + str(digito_senha3) + str(digito_senha4)
print("")
print("===== GERADOR DE SENHA =====")
print(f"usuário: {nome_usuario}")
print(f"Sua senha de acesso é: {senha}")
print("============================")