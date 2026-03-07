troco = float(input("Valor do troco: R$"))
nota_50 = troco // 50
resto_50 = troco % 50

nota_20 = resto_50 // 20
resto_20 = resto_50 % 20

nota_10 = resto_20 // 10
resto_10 = resto_20 % 10

nota_1 = resto_10 // 1

print(f"Valor do troco: R${troco:.2f}") 
print("Notas de R$50:", int(nota_50))
print("Notas de R$20:", int(nota_20))
print("Notas de R$10:", int(nota_10))
print("Notas de R$1:", int(nota_1))
