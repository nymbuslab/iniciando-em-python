"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão

1 para binário
2 para octal
3 para hexadecimal
"""

numero = int(input("Digite um número inteiro qualquer: "))
base_conversao = input(
    "Escolha uma das opções para converte: \n[1] Binário\n[2] Octal\n[3] Hexadecimal"
).strip()

if base_conversao not in ["1", "2", "3"]:
    print("Escolha uma opção válida")
if numero < 0:
    print("Número negativo não permitido")
elif base_conversao == "1":
    print(f"O número {numero} convertido para binário é: {bin(numero)[2:]}")
elif base_conversao == "2":
    print(f"O número {numero} convertido para octal é: {oct(numero)[2:]}")
elif base_conversao == "3":
    print(f"O número {numero} convertido para hexadecimal é: {hex(numero)[2:]}")
