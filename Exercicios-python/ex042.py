from random import random

'''Uma empresa precisa gerar crachás digitais para seus funcionários. Peça nome completo e cargo. O sistema deve exibir:

Nome em title() sem espaços extras
Iniciais do nome (ex: Carlos Silva → C.S.)
Cargo em maiúsculas
Um código de crachá gerado com os 3 primeiros caracteres do nome + 4 números aleatórios'''

nome = input("Nome do funcionário: ").strip() .title()
iniciais = nome.split()[0][0] + "." + nome.split()[-1][0] + "."
cargo = input("Digite o cargo: ").upper()
codigo_cracha = nome[:3].upper() + str(int(random() * 10000)).zfill(4)

print("======= CRACHÁ DIGITAL =======")
print(f"Nome: {nome}")
print(f"Iniciais: {iniciais}")
print(f"Cargo: {cargo}")
print(f"Código: {codigo_cracha}")
print("==============================")