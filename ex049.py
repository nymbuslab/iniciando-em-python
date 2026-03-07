valor_inicial = float(input('Digite o valor do investimento: R$'))
taxa = int(input('Taxa de Juros (%): '))
anos = int(input('Resgate em quantos anos: '))
montante = valor_inicial * (1 + (taxa/100) * anos)

print(montante)