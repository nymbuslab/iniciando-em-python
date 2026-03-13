"""
Escreva um programa que leia a velocidade de um carro,
Se ele ultrapassar 80km/h, mestre uma mensagem dizendo que ele foi multado.

A multa vai custar R$7.00 por cada km acima do limite
"""

velocidade_permitida = 80
velocidade_veiculo = float(input("Qual a velocidade do veiculo: "))

if velocidade_veiculo > velocidade_permitida:
    multa = (velocidade_veiculo - velocidade_permitida) * 7
    print("Você excedeu a velocidade permitida da via, você foi MULTADO!")
    print(f"Valor da multa: R${multa:.2f}")
else:
    print("Velocidade dentro do permitido. Boa viagem!")
