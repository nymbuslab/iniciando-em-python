"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- Entre 25 até 30: Sobrepeso
- Entre 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""

VERMELHO = "\033[31m"
VERDE = "\033[32m"
AMARELO = "\033[33m"
AZUL = "\033[34m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

import time

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

# Sugestão
if imc < 18.5:
    status = f"{AMARELO}Abaixo do Peso{RESET}"  # amarelo → atenção
elif imc < 25:
    status = f"{VERDE}Peso ideal{RESET}"  # verde → ok
elif imc < 30:
    status = f"{AMARELO}Sobrepeso{RESET}"  # amarelo → atenção
elif imc < 40:
    status = f"{VERMELHO}Obesidade{RESET}"  # vermelho → perigo
else:
    status = f"{VERMELHO}Obesidade mórbida!{RESET}"  # vermelho → perigo grave

print(f"Peso do paciente: {peso:.2f} kg")
print(f"Altura do paciente: {altura:.2f} m")
print("Calculando IMC, aguarde...")
time.sleep(2)
print("Calculando...")
time.sleep(1)
print(f"IMC: {imc:.2f}")
print(f"Status: {status}")
