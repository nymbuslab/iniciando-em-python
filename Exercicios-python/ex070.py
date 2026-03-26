"""
Peça nome, peso e altura. Calcule o IMC e classifique usando in para verificar a faixa. Exiba a ficha completa com datetime para a data de hoje:

- Abaixo de 18.5 → Abaixo do peso
- 18.5 a 24.9 → Peso normal
- 25.0 a 29.9 → Sobrepeso
- 30.0 ou mais → Obesidade
"""
from datetime import date

nome_paciente = input("Nome do paciente: ").strip() .title()
data_consulta = date.today()
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura * altura)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc  < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "IMC superior a 30, procure um médico com urgência"
    
print(f"Paciente: {nome_paciente}")
print(f"Data: {data_consulta.day:02d}/{data_consulta.month:02d}/{data_consulta.year}")
print(f"Peso: {peso:.2f}kg")
print(f"Altura: {altura:.2f}m")
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")