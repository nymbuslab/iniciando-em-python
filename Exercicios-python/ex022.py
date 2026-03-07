moeda_br = float(input("Digite o valor (Real-Br): R$"))
moeda_us = float(input("Digite o valor do dólar (Cotação atual): U$"))
moeda_eu = float(input("Digite o valor do euro (Cotação atual): €"))
conversao_dolar = moeda_br / moeda_us
conversao_euro = moeda_br / moeda_eu

print("")
print("===== CONVERSOR =====")
print(f"Valor em reais: R${moeda_br:.2f}")
print(f"Valor em dólar: U${conversao_dolar:.2f}")
print(f"Valor em euro: €{conversao_euro:.2f}")
print("=====================")