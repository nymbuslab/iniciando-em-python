'''
Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros
'''

valor_metros = float(input("Digite o valor da medida (metros): "))

print("===== Conversor =====")
print("")
print("Medida: " + str(valor_metros) + "/m")
print("Convertido para centímetros: " + str(valor_metros * 100) + " cm")
print("Convertido para milímetros: " + str(valor_metros * 1000) + " mm")
