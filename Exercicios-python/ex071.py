"""
Uma lanchonete tem o seguinte cardápio:

- X-Burguer: R$15.00
- X-Salada: R$18.00
- X-Bacon: R$22.00

Peça o nome do cliente e o item desejado com `in` para validar. Pergunte se vai querer bebida (+R$5.00) e sobremesa (+R$7.00) usando ternário. Exiba o recibo completo.
"""

nome_cliente = input("Digite o seu nome: ").strip().title()
print(
    """
=======================
   ESCOLHA SEU LANCHE 
=======================
[1]X-Burguer....R$15.00
[2]X-Salada.....R$18.00
[3]X-Bacon......R$22.00
=======================
       OPCIONAIS
=======================
[4]SUCO.........R$ 5.00
[5]SOBREMESA....R$ 7.00
=======================
"""
)
opcao_lanche = input("Qual a sua opção de lanche: ").strip()
opcional_bebida = input("Deseja bebida (S/N):").strip() .upper()
opcional_sobremesa = input("Deseja Sobremesa (S/N):").strip() .upper()

if opcao_lanche not in ["1", "2", "3"]:
    lanche = "Opção inválida"
    preco_lanche = 0
    
elif opcao_lanche == "1":
    lanche = "X-Burguer.....R$15.00"
    preco_lanche = 15.0

elif opcao_lanche == "2":
    lanche = "X-Salada.....R$18.00"
    preco_lanche = 18.00
    
elif opcao_lanche == "3":
    lanche = "X-Bacon.....R$22.00"
    preco_lanche = 22.00
    
valor_bebida = 5.00 if opcional_bebida == "S" else 0
valor_sobremesa = 7.00 if opcional_sobremesa == "S" else 0
total = preco_lanche + valor_bebida + valor_sobremesa
    
print("\n")
print("====== LANCHONETE ======")
print(f"Cliente: {nome_cliente}")
print(f"Lanche: {lanche}")
if opcional_bebida == "S":
    print(f"Bebida: Sim | +R${valor_bebida:.2f}")
else:
    print("Bebida: Não")
if opcional_sobremesa == "S":
    print(f"Sobremesa: Sim | +R${valor_sobremesa:.2f}")
else:
    print("Sobremesa: Não")
print(f"Total: R${total:.2f}")

