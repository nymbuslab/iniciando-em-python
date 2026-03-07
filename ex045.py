celsius = float(input('Digite a temperatura em graus Celsius: '))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

if celsius < 0:
    estado = 'Abaixo do ponto de congelamento'
elif celsius < 100:
    estado = 'Entre congelamento e ebulição'
else:
    estado = 'Acima do ponto de ebulição'

print(f'Temperatura: {celsius:.2f}°C')
print(f'Em Fahrenheit: {fahrenheit:.2f}°F')
print(f'Em Kelvin: {kelvin:.2f}K')
print(f'Estado: {estado}')