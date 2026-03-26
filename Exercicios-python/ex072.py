"""
Simule um caixa eletrônico. Peça nome do cliente, saldo atual e valor do saque. Verifique:

- Saldo deve ser maior que zero
- Valor do saque deve ser maior que zero
- Valor do saque não pode ser maior que o saldo
- Valor do saque deve ser múltiplo de 20 (use `%`)

Se aprovado, mostre o saldo restante. Se negado, informe o motivo.
"""

nome_cliente = input("Nome do cliente: ").strip().title()
saldo_conta = float(input("Saldo Atual: R$ "))
valor_saque = float(input("Valor do saque: R$ "))

if saldo_conta > 0:
    if valor_saque <= 0:
        status = "Valor de saque inválido"
    elif valor_saque > saldo_conta:
        status = "Saldo insuficiente"
    elif valor_saque % 20 != 0:
        status = "Valor deve ser múltiplo de R$20"
    else:
        status = "APROVADO"
else:
    status = "Conta sem saldo"

saldo_restante = saldo_conta - valor_saque if status == "APROVADO" else saldo_conta

print("===== CAIXA ELETRÔNICO =====")
print(f"Cliente: {nome_cliente}")
print(f"Saldo atual: R${saldo_conta:.2f}")
print(f"Valor do saque: R${valor_saque:.2f}")
print(f"Status: {status}")
print(f"Saldo em conta: {saldo_restante:.2f}")
print("============================")
