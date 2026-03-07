nome_usuario = input("Digite seu nome Completo: ")
email = input("Digite seu email: ")

if "@" in email:
    status = "E-mail válido"
else:
    status = "E-mail inválido"

print("\n")
print("===== Dados inseridos =====")
print(f"Nome: {nome_usuario}")
print(f"E-mail: {email}")
print("\n")
print("===== Dados corrigidos =====")
print(f"Nome: {nome_usuario.title()}")
print(f"E-mail: {email.lower()}")
print(f"Caracteres no e-mail: {len(email)}")
print(f"Status: {status}")
