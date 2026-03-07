'''
Faça um programa que leia o comprimento do cateto oposto e o cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''

from math import sqrt, pow, hypot

cateto_oposto = float(input("Informe o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Informe o comprimento do cateto adjacente: "))
'''
soma_catetos = (pow(cateto_oposto, 2) + pow(cateto_adjacente, 2))
hipotenusa = hypot(soma_catetos)
'''

hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f"Se um triângulo retângulo possui catetos de medidas {cateto_oposto:.2f} cm e {cateto_adjacente:.2f} cm:")
print(f"A hipotenusa mede {hipotenusa:.2f} cm")