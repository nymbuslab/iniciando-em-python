numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))
operador = input('Digite a operação (+, -, *, /): ').strip()

if operador == '+':
    resultado = numero1 + numero2
elif operador == '-':
    resultado = numero1 - numero2
elif operador == '*':
    resultado = numero1 * numero2
elif operador == '/':
    if numero2 == 0:
        resultado = 'Erro: divisão por zero!'  # atribui à variável, não imprime
    else:
        resultado = numero1 / numero2
else:
    resultado = 'Escolha um operador válido'

print(f'Número 1: {numero1:.2f}')
print(f'Número 2: {numero2:.2f}')
print(f'Operação: {operador}')
if isinstance(resultado, str):
    print(resultado)                  # exibe mensagem de erro ou aviso
else:
    print(f'Resultado: {numero1:.2f} {operador} {numero2:.2f} = {resultado:.2f}')