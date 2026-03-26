
#Mostra na tela os números de 1 até 10.
for numero in range(1, 11):
    print(numero)
    
#Mostra os números pares de 0 até 20.
for numero in range(0, 21):
    if numero % 2 == 0:
        print(numero)

#Mostra os números pares de 0 até 20.
for numero in range(0, 21, 2):
    print(numero)
    
#Peça 5 números ao usuário e mostre a soma deles.
soma = 0

for contador in range(5):
    numero = int(input("Digite um número: "))
    soma = soma + numero
print(f"O total da soma foi: {soma}")

#Faça uma contagem regressiva de 10 até 1.

for regressivo in range(10, 0, -1):
    print(regressivo)

#Peça 4 nomes e mostre uma mensagem para cada um.

for i in range(4):
    nome = input("Digite o nome do usuário: ").strip().title()
    print(f"Olá, {nome}")
print("Fim do loop")
    