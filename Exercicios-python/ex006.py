"""
Peça dois números ao usuário e exiba o resultado das 7 operações aritméticas entre eles.

Número 1: 10
Número 2: 3
Soma: 13
Subtração: 7
Multiplicação: 30
Divisão: 3.3333333333333335
Divisão inteira: 3
Resto: 1
Potência: 1000
"""

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("")
print("Número 1:", num1)
print("Número 2:", num2)
print("")
print("===== Resultados =====")
print("Soma: ", num1 + num2)
print("Subtração: ", num1 - num2)
print("Multiplicação: ", num1 * num2)
print("Divisão: ", num1 / num2)
print("Divisão inteira: ", num1 // num2)
print("Resto: ", num1 % num2)
print("Potência: ", num1 ** num2)
