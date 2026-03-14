from datetime import datetime

usuario_padrao = "pabllomartins"
senha_padrao = "123456"
hora_acesso = datetime.now()

usuario = input("Digite o nome do usuário: ").lower().strip()
senha = input("Digite a senha: ").strip()

if usuario_padrao != usuario:
    print("\nUsuário não encontrado")
elif senha_padrao != senha:
    print("Senha incorreta, tente novamente!")
else:
    print("Seja bem-vindo\n")
    print(f"Usuário: {usuario}")
    print(f"Senha: {senha}")
    print(
        f"Acesso em: {hora_acesso.day:02d}/{hora_acesso.month:02d}/{hora_acesso.year} às {hora_acesso.hour:02d}:{hora_acesso.minute:02d}"
    )
