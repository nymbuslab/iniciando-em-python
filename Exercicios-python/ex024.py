import math

num_raiz = float(input("Digite um número: "))
raiz = math.sqrt(num_raiz)
potencia = math.pow(num_raiz, 3)
print("")
print(f"Número digitado: {num_raiz}")
print(f"Raiz quadrada de {num_raiz} é: {raiz:.2f}")
print(f"Arredondamento pra cima: {math.ceil(num_raiz)}")
print(f"Arredondamento pra baixo: {math.floor(num_raiz)}")
print(f"Cubo: {potencia:.0f}")