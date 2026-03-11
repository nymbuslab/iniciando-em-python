nome_cliente = input("Digite o nome do cliente: ").strip().title()
cep = input("Digite o cep: ").strip()  # string direto
valor_compra = float(input("Digite o valor da compra: R$"))

if valor_compra > 200:
    frete = "Frete Grátis"
elif cep[0] == "0" or cep[0] == "1":  # sem str() pois já é string
    frete = 15.00
elif cep[0] == "2" or cep[0] == "3":
    frete = 25.00
else:
    frete = 40.00

print("\n")
print("===== CALCULO DE FRETE =====")
print(f"Nome: {nome_cliente}")
print(f"CEP: {cep[0:2]}.{cep[2:5]}-{cep[5:8]}")  # sem str() pois já é string
print(f"Valor da compra: R${valor_compra:.2f}")

if isinstance(frete, str):
    print(f"Frete: {frete}")
else:
    print(f"Frete: R${frete:.2f}")
    print(f"Total: R${valor_compra + frete:.2f}")
print("============================")
