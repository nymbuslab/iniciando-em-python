"""
Validador de Senha
Um sistema precisa validar senhas cadastradas. Peça uma senha ao usuário e verifique:

Se tem pelo menos 8 caracteres → "Tamanho OK" ou "Senha muito curta"
Se contém "@" ou "#" → "Contém caractere especial" ou "Sem caractere especial"
Exiba a senha com os caracteres do meio substituídos por * — mantendo apenas o primeiro e o último caractere visíveis
"""

senha = input("Crie uma senha: ").strip()

if len(senha) >= 8:
    tamanho_senha = "Tamanho OK"
else:
    tamanho_senha = "Senha muito curta"

if "@" in senha or "#" in senha:
    caracteres = "Contém caractere especial"
else:
    caracteres = "Sem caractere especial"

senha_mascarada = senha[0] + "*" * (len(senha) - 2) + senha[-1]

print(f"Tamanho: {tamanho_senha}")
print(f"Caractere especial: {caracteres}")
print(f"Senha exibida: {senha_mascarada}")
