'''
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que a cada litro de tinta, pinta uma área de 2m
'''

largura = float(input("Digite a largura de parede(em metros):"))
altura = float(input("Digite a altura da parede (em metros): "))
area_parede = altura * largura
qtd_litros = area_parede / 2

print("Altura da parede:", altura, "m")
print("Largura da parede:", largura, "m")
print("Área da parede:", area_parede)
print("Quantidade de litros para pintar a parede é de:", qtd_litros, "Litros")
