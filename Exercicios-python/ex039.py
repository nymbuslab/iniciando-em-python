"""
Crie um programa que leia o nome completo de uma pessoa e mostre
- O nome com todas as letras maiúsculas
- O noe com todas as letras minúsculas
- Quantas letras tem (sem considerar espaços)
- Quantas letras tem o primeiro nome
"""

nome_completo = input("Digite o nome completo: ").strip()

print(f"Nome completo em letras maiúsculas: {nome_completo.upper()}")
print(f"Nome completo em letras minúsculas: {nome_completo.lower()}")
# print(f"Quantidade de Caracteres (Desconsiderando espaços: {len(nome_completo.replace(' ', '')  )}")
# uma abordagem que o professor usou que ao invés de usar o replace como eu fiz ele usou count
print(
    f"Quantidade de Caracteres (Desconsiderando espaços: {len(nome_completo) - nome_completo.count(' ')}"
)
print(
    f"Seu primeiro nome é {nome_completo.split()[0]} e tem {len(nome_completo.split()[0])} letras"
)
