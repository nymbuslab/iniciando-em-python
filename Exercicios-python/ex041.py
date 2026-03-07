'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Exemplo: 1834
Unidade: 4 dezena: 3 centena: 8 milhar: 1'''

'''numero = input("Digite um número de 0 a 9999: ")

print(f"Unidade: {numero[3]}")
print(f"Dezena: {numero[2]}")
print(f"Centena: {numero[1]}")
print(f"Milhar: {numero[0]}")'''

#Resolvi o exercício acima desta forma porém dava erro caso eu nao digitasse todos os números

#Solução do professor

'''numero = int(input("Digite um número de 0 a 9999: "))
un = numero // 1 % 10
dz = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print(f"Unidade: {un}")
print(f"Dezena: {dz}")
print(f"Centena: {cen}")
print(f"Milhar: {mil}")'''

#Ok o exercicio deu certo, mas perdeu o sentido da atividade que e formatação de string, como faria isso com string?

#Solução usando zfill

numero = input("Digite um número de 0 a 9999: ")

# zfill(4) preenche com zeros à esquerda até ter 4 dígitos
numero = numero.zfill(4)
# "5"    → "0005"
# "83"   → "0083"
# "834"  → "0834"
# "1834" → "1834"

print(f"Unidade: {numero[-1]}")  # ou numero[3]
print(f"Dezena: {numero[-2]}")
print(f"Centena: {numero[-3]}")
print(f"Milhar: {numero[-4]}")