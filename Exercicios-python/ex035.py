frase = input("Escreva uma frase qualquer: ")


print("\n")
print("===== Analisador de Frase =====")
print(f"Frase: {frase}")
print(f"Caracteres sem espaço: {len(frase.replace(' ', ''))}")
print(f"Letra 'a' aparece: {frase.lower() .count("a")} vezes")
print(
    f"Frase codificada: {frase.lower() .replace('a', '*') .replace('e', '*') .replace('i', '*') .replace('o', '*') .replace('u', '*')}"
)
